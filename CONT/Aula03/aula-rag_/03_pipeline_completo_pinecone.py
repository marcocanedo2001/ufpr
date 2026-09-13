from pathlib import Path
import os
import time
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer


load_dotenv()

API_KEY = os.getenv("PINECONE_API_KEY")
# Nome do índice que será criado ou reutilizado no Pinecone.
NOME_INDICE = "documentos-academicos"
# Namespace usado para separar logicamente os vetores dentro do índice.
#
# Um mesmo índice pode possuir diferentes namespaces, por exemplo:
#
# aula-rag
# turma-2026
# regulamentos
# artigos
NAMESPACE = "aula-rag"
# Dimensão dos vetores gerados pelo modelo escolhido.
#
# O modelo paraphrase-multilingual-MiniLM-L12-v2 gera embeddings
# com 384 dimensões.
DIMENSAO = 384
# Quantidade máxima de caracteres em cada chunk.
TAMANHO_CHUNK = 800
# Quantidade de caracteres repetidos entre chunks consecutivos.
#
# A sobreposição ajuda a preservar informações que aparecem
# na fronteira entre dois chunks.
SOBREPOSICAO = 150
# Modelo de embeddings multilíngue executado localmente.
MODELO = (
    "sentence-transformers/"
    "paraphrase-multilingual-MiniLM-L12-v2"
)
#Extrai o texto das páginas
def carregar_pdf(caminho: Path) -> list[dict]:
    leitor = PdfReader(caminho)
    paginas = []

      # Ignora páginas vazias ou contendo somente espaços.
    for numero, pagina in enumerate(leitor.pages, start=1):
        texto = pagina.extract_text() or ""

        if texto.strip():
            paginas.append(
                {
                    "fonte": caminho.name,
                    "pagina": numero,
                    "texto": texto.strip(),
                }
            )

    return paginas


def gerar_chunks(
    texto: str,
    tamanho: int = TAMANHO_CHUNK,
    sobreposicao: int = SOBREPOSICAO,
) -> list[str]:
    """
    Divide um texto em trechos menores com sobreposição.

    Exemplo:

    texto:
        ABCDEFGHIJKLMNOP

    tamanho:
        8

    sobreposição:
        3

    resultado aproximado:
        ABCDEFGH
             FGHIJKLM
                  KLMNOP

    Parâmetros
    ----------
    texto:
        Texto que será dividido.

    tamanho:
        Quantidade máxima de caracteres em cada chunk.

    sobreposicao:
        Quantidade de caracteres compartilhados por dois
        chunks consecutivos.

    Retorno
    -------
    list[str]:
        Lista de chunks.
    """

    # A sobreposição precisa ser menor que o tamanho do chunk.
    #
    # Caso contrário, o algoritmo não avançaria no texto
    # e poderia entrar em um laço infinito.

    if tamanho <= sobreposicao:
        raise ValueError(
            "O tamanho deve ser maior que a sobreposição."
        )
     # Lista que armazenará os chunks gerados.
    chunks = []
    inicio = 0

     # Continua enquanto ainda houver texto para processar.
    while inicio < len(texto):
        fim = min(inicio + tamanho, len(texto))
        trecho = texto[inicio:fim].strip()

        if trecho:
            chunks.append(trecho)

        if fim == len(texto):
            break
        # O próximo chunk começa antes do final do chunk atual.
        #
        # Isso cria a sobreposição.
        inicio = fim - sobreposicao

    return chunks


def criar_indice(
    pc: Pinecone,
) -> None:
    """
    Cria o índice no Pinecone caso ele ainda não exista.

    O índice é configurado com:

    - 384 dimensões;
    - similaridade de cosseno;
    - arquitetura serverless;
    - AWS;
    - região us-east-1.
    """

    # Verifica se já existe um índice com o nome informado.
    #
    # Se existir, não é necessário criá-lo novamente.
    if pc.has_index(NOME_INDICE):
        return

    # Solicita a criação do índice no Pinecone.
    pc.create_index(
        name=NOME_INDICE,
        # Deve ser igual à dimensão produzida pelo
        # modelo de embeddings.
        dimension=DIMENSAO,
        # Métrica utilizada para comparar os vetores.
        metric="cosine",
         # Configuração da infraestrutura serverless.
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1",
        ),
    )
     # A criação do índice é assíncrona.
    #
    # O código consulta o status periodicamente até que
    # o índice esteja disponível.
    while not pc.describe_index(
        NOME_INDICE
    ).status["ready"]:
        print("Aguardando índice...")
        time.sleep(2)


def indexar_pdf(
    index,
    modelo: SentenceTransformer,
    caminho_pdf: Path,
) -> None:
    """
    Executa o processo completo de indexação de um PDF.

    Fluxo:

    PDF
      → páginas
      → chunks
      → embeddings
      → registros
      → Pinecone

    Parâmetros
    ----------
    index:
        Referência para o índice do Pinecone.

    modelo:
        Modelo SentenceTransformer utilizado para gerar embeddings.

    caminho_pdf:
        Caminho do arquivo PDF.
    """
     # Lista que armazenará todos os chunks e seus metadados.
    registros = []

    for pagina in carregar_pdf(caminho_pdf):
        chunks = gerar_chunks(pagina["texto"])

         # Percorre os chunks produzidos para a página.
        for numero_chunk, chunk in enumerate(chunks):
            registros.append(
                {
                    # Cria um identificador único para o chunk.
                    #
                    # Exemplo:
                    # 2024-regulamento-estagio-p3-c2
                    #
                    # Significa:
                    # documento: 2024-regulamento-estagio
                    # página: 3
                    # chunk: 2
                    "id": (
                        f"{caminho_pdf.stem}"
                        f"-p{pagina['pagina']}"
                        f"-c{numero_chunk}"
                    ),
                     # Texto que será transformado em embedding.
                    "texto": chunk,
                     # Nome do arquivo original.
                    "fonte": pagina["fonte"],
                    # Página de origem do chunk.
                    "pagina": pagina["pagina"],
                    # Posição do chunk dentro da página.
                    "chunk": numero_chunk,
                }
            )
    # Gera um embedding para cada chunk.
    #
    # normalize_embeddings=True normaliza os vetores.
    # Isso é adequado quando se utiliza similaridade de cosseno.
    embeddings = modelo.encode(
        [item["texto"] for item in registros],
        normalize_embeddings=True,
        show_progress_bar=True,
    )
     # Prepara os objetos no formato esperado pelo Pinecone.
    vetores = [
        {
            "id": item["id"],
            "values": embedding.tolist(),
            # Informações associadas ao vetor.
            #
            # Os metadados podem ser retornados na consulta
            # e utilizados em filtros.
            "metadata": {
                "texto": item["texto"],
                "fonte": item["fonte"],
                "pagina": item["pagina"],
                "chunk": item["chunk"],
                "tipo": "regulamento",
                "vigente": True,
            },
        }
        for item, embedding in zip(
            registros,
            embeddings,
        )
    ]
     # Envia os vetores ao Pinecone em lotes de 100.
    #
    # O envio em lotes é mais eficiente do que realizar
    # uma requisição individual para cada vetor.
    for inicio in range(0, len(vetores), 100):
        # upsert:
        #
        # - insere um registro novo quando o ID não existe;
        # - substitui o registro quando o ID já existe.
        index.upsert(
            vectors=vetores[inicio:inicio + 100],
            namespace=NAMESPACE,
        )

    print(
        f"{len(vetores)} chunks enviados para o Pinecone."
    )


def buscar(
    index,
    modelo: SentenceTransformer,
    pergunta: str,
    top_k: int = 5,
) -> None:
    """
    Executa uma busca semântica no Pinecone.

    A pergunta é transformada em embedding usando o mesmo
    modelo empregado na indexação.

    Parâmetros
    ----------
    index:
        Índice do Pinecone.

    modelo:
        Modelo usado para gerar o embedding da pergunta.

    pergunta:
        Pergunta informada pelo usuário.

    top_k:
        Quantidade máxima de resultados retornados.
    """
     # Transforma a pergunta em um vetor.
    embedding = modelo.encode(
        pergunta,
        normalize_embeddings=True,
    ).tolist()

    resposta = index.query(
        namespace=NAMESPACE,
        vector=embedding,
        top_k=top_k,
        include_metadata=True,
        # Não retorna os 384 valores de cada embedding.
        #
        # Isso reduz a quantidade de dados transferida.
        include_values=False,
         # Considera somente documentos marcados como vigentes.
        filter={
            "vigente": {"$eq": True},
        },
    )

    print(f"\nPergunta: {pergunta}\n")

    for posicao, resultado in enumerate(
        resposta["matches"],
        start=1,
    ):
        metadata = resultado["metadata"]

        # Score representa a similaridade entre o embedding
        # da pergunta e o embedding do chunk.
        print(
            f"{posicao}. score={resultado['score']:.4f}"
        )
        print(
            f"   {metadata['fonte']} "
            f"— página {metadata['pagina']}"
        )
        # Exibe somente os primeiros 500 caracteres
        # para evitar uma saída excessivamente longa.
        print(
            f"   {metadata['texto'][:500]}"
        )
        print()


def main() -> None:
    if not API_KEY:
        raise RuntimeError(
            "Defina PINECONE_API_KEY no arquivo .env."
        )

    caminho_pdf = Path(
        "data/documentos/2024-regulamento-estagio.pdf"
    )

    if not caminho_pdf.exists():
        raise FileNotFoundError(
            f"Arquivo não encontrado: {caminho_pdf}"
        )

    pc = Pinecone(api_key=API_KEY)
    criar_indice(pc)

    descricao = pc.describe_index(NOME_INDICE)
    index = pc.Index(host=descricao.host)

    modelo = SentenceTransformer(MODELO)

    indexar_pdf(
        index,
        modelo,
        caminho_pdf,
    )
    while True:
            pergunta = input(
                "\nDigite sua pergunta ou 'sair': "
            ).strip()

            if pergunta.lower() == "sair":
                print("Programa encerrado.")
                break

            if not pergunta:
                print("Digite uma pergunta válida.")
                continue

        

            buscar(
                index,
                modelo,
                pergunta,
            )


if __name__ == "__main__":
    main()