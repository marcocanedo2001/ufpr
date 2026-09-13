from pathlib import Path
from time import perf_counter
import re

import chromadb
import numpy as np
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer


# ============================================================
# CONFIGURAÇÕES
# ============================================================

PASTA_DOCUMENTOS = Path("data/documentos")
PASTA_CHROMA = Path("chroma_db")

NOME_COLECAO = "documentos_academicos_aula"

MODELO_EMBEDDING = (
    "sentence-transformers/"
    "paraphrase-multilingual-MiniLM-L12-v2"
)

TAMANHO_CHUNK = 800
OVERLAP_CHUNK = 150
TAMANHO_LOTE = 32
TOP_K = 3

# Use "similaridade" ou mmr.
MODO_BUSCA = "similaridade"

# O MMR recupera primeiro um conjunto maior de candidatos
# e seleciona k resultados equilibrando relevância e diversidade.
FETCH_K_MMR = 12
LAMBDA_MMR = 0.6

# Na primeira execução, deixe True.
# Depois, altere para False para persistência.
RECRIAR_COLECAO = True


# ============================================================
# INGESTÃO: LEITURA E LIMPEZA DOS PDFS
# ============================================================

def normalizar_texto(texto: str) -> str:
    texto = texto.replace("\u00a0", " ")
    texto = texto.replace("\r\n", "\n")
    texto = texto.replace("\r", "\n")
    texto = re.sub(r"[ \t]+", " ", texto)
    texto = re.sub(r"\n\s*\n+", "\n\n", texto)
    return texto.strip()


def carregar_pdfs(pasta: Path) -> list[dict]:
    if not pasta.exists():
        raise FileNotFoundError(
            f"A pasta não existe: {pasta.resolve()}"
        )

    arquivos = sorted(pasta.glob("*.pdf"))

    if not arquivos:
        raise FileNotFoundError(
            f"Nenhum PDF encontrado em: {pasta.resolve()}"
        )

    paginas = []

    for arquivo in arquivos:
        print(f"Lendo: {arquivo.name}")
        reader = PdfReader(str(arquivo))

        for numero_pagina, pagina in enumerate(
            reader.pages,
            start=1,
        ):
            texto = normalizar_texto(
                pagina.extract_text() or ""
            )

            if not texto:
                print(
                    f"  Aviso: página {numero_pagina} "
                    "sem texto extraível."
                )
                continue

            paginas.append(
                {
                    "arquivo": arquivo.name,
                    "pagina": numero_pagina,
                    "texto": texto,
                }
            )

    return paginas


# ============================================================
# TODO 1 — CHUNKING.
# ============================================================

def gerar_chunks(
    texto: str,
    tamanho: int = TAMANHO_CHUNK,
    overlap: int = OVERLAP_CHUNK,
) -> list[str]:
    """
    Divida o texto em janelas de caracteres.

    Requisitos:
    1. overlap deve ser menor que tamanho;
    2. use passo = tamanho - overlap;
    3. ignore chunks vazios;
    4. retorne uma lista de strings.
    """

    # TODO 1.1: validar tamanho e overlap.
    # TODO 1.2: criar a lista de chunks.
    # TODO 1.3: percorrer o texto usando uma janela.
    # TODO 1.4: avançar pelo passo correto.
    # TODO 1.5: retornar os chunks.

    raise NotImplementedError(
        "Implemente gerar_chunks()."
    )


def preparar_chunks(paginas: list[dict]) -> list[dict]:
    todos_chunks = []

    for pagina in paginas:
        chunks_da_pagina = gerar_chunks(
            pagina["texto"],
            tamanho=TAMANHO_CHUNK,
            overlap=OVERLAP_CHUNK,
        )

        nome_base = Path(pagina["arquivo"]).stem

        for numero_chunk, texto_chunk in enumerate(
            chunks_da_pagina,
            start=1,
        ):
            identificador = (
                f"{nome_base}"
                f"_p{pagina['pagina']:03d}"
                f"_c{numero_chunk:03d}"
            )

            todos_chunks.append(
                {
                    "id": identificador,
                    "arquivo": pagina["arquivo"],
                    "pagina": pagina["pagina"],
                    "numero_chunk": numero_chunk,
                    "texto": texto_chunk,
                }
            )

    return todos_chunks


# ============================================================
# TODO 2 — BANCO VETORIAL
# Criar a coleção com distância de cosseno.
# ============================================================

def criar_colecao(recriar: bool):
    PASTA_CHROMA.mkdir(parents=True, exist_ok=True)

    client = chromadb.PersistentClient(
        path=str(PASTA_CHROMA)
    )

    if recriar:
        try:
            client.delete_collection(NOME_COLECAO)
        except Exception:
            # A coleção ainda pode não existir.
            pass

    # TODO 2.1: usar get_or_create_collection.
    # TODO 2.2: definir a configuração HNSW com space="cosine".
    # configuration={"hnsw": {"space": "cosine"}}

    raise NotImplementedError(
        "Implemente criar_colecao() durante a aula."
    )


# ============================================================
# TODO 3 — EMBEDDINGS E INDEXAÇÃO
# ============================================================

def indexar_chunks(
    collection,
    modelo: SentenceTransformer,
    chunks: list[dict],
) -> None:
    if not chunks:
        raise ValueError("Não existem chunks para indexar.")

    total = len(chunks)
    inicio_total = perf_counter()

    for inicio in range(0, total, TAMANHO_LOTE):
        fim = min(inicio + TAMANHO_LOTE, total)
        lote = chunks[inicio:fim]

        textos = [chunk["texto"] for chunk in lote]

        # TODO 3.1:
        # Gere os embeddings de todos os textos do lote.
        # Use:
        # - batch_size=TAMANHO_LOTE
        # - normalize_embeddings=True
        # - show_progress_bar=False

        # TODO 3.2:
        # Grave o lote usando collection.upsert().
        # Envie:
        # - ids;
        # - embeddings;
        # - documents;
        # - metadatas com arquivo, página e número do chunk.

        raise NotImplementedError(
            "Implementar."
        )

    tempo = perf_counter() - inicio_total
    print(f"Indexação concluída em {tempo:.2f} s.")


# ============================================================
# TODO 4 — BUSCA VETORIAL
# ============================================================

def buscar(
    collection,
    modelo: SentenceTransformer,
    pergunta: str,
    k: int = TOP_K,
) -> dict:
    pergunta = pergunta.strip()

    if not pergunta:
        raise ValueError("A pergunta não pode estar vazia.")

    # TODO 4.1:
    # Gere o embedding normalizado da pergunta.

    # TODO 4.2:
    # Execute collection.query() com:
    # - query_embeddings;
    # - n_results=k;
    # - include=["documents", "metadatas", "distances"].

    # TODO 4.3:
    # Meça a latência usando perf_counter() e inclua
    # resultados["latencia_ms"] e resultados["pergunta"].

    raise NotImplementedError(
        "Implemente buscar()."
    )


# ============================================================
# TODO 6 — EXTENSÃO: MAXIMAL MARGINAL RELEVANCE
# ============================================================

def buscar_mmr(
    collection,
    modelo: SentenceTransformer,
    pergunta: str,
    k: int = TOP_K,
    fetch_k: int = FETCH_K_MMR,
    lambda_mult: float = LAMBDA_MMR,
) -> dict:
    """
    Recupera fetch_k candidatos por similaridade e seleciona k
    resultados equilibrando relevância e diversidade.

    Fórmula:
        lambda * sim(chunk, pergunta)
        - (1 - lambda) * max sim(chunk, selecionados)
    """

    # TODO 6.1: validar pergunta, k, fetch_k e lambda_mult.
    # TODO 6.2: gerar o embedding normalizado da pergunta.
    # TODO 6.3: consultar fetch_k candidatos, incluindo embeddings.
    # TODO 6.4: selecionar primeiro o candidato mais relevante.
    # TODO 6.5: selecionar os demais penalizando redundância.
    # TODO 6.6: devolver os resultados no mesmo formato de buscar().

    raise NotImplementedError(
        "Implemente buscar_mmr()"
    )


# ============================================================
# EXIBIÇÃO
# ============================================================

def imprimir_resultados(resultados: dict) -> None:
    documentos = resultados["documents"][0]
    metadados = resultados["metadatas"][0]
    distancias = resultados["distances"][0]
    ids = resultados["ids"][0]

    print("\n" + "#" * 80)
    print(f"Pergunta: {resultados['pergunta']}")
    print(
        "Latência da busca: "
        f"{resultados['latencia_ms']:.2f} ms"
    )
    print("#" * 80)

    for rank, (
        identificador,
        texto,
        metadata,
        distancia,
    ) in enumerate(
        zip(
            ids,
            documentos,
            metadados,
            distancias,
        ),
        start=1,
    ):
        similaridade = 1 - distancia

        print("\n" + "=" * 80)
        print(f"Rank: {rank}")
        print(f"ID: {identificador}")
        print(f"Arquivo: {metadata['arquivo']}")
        print(f"Página: {metadata['pagina']}")
        print(f"Chunk: {metadata['numero_chunk']}")
        print(f"Distância de cosseno: {distancia:.4f}")
        print(f"Similaridade aproximada: {similaridade:.4f}")
        print("-" * 80)
        print(texto[:1200])


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

def main() -> None:
    print("1. Carregando PDFs...")
    paginas = carregar_pdfs(PASTA_DOCUMENTOS)
    print(f"Páginas com texto: {len(paginas)}")

    print("\n2. Gerando chunks...")
    chunks = preparar_chunks(paginas)
    print(f"Total de chunks: {len(chunks)}")

    print("\n3. Carregando o modelo de embeddings...")

    # TODO 5:
    # Crie o objeto SentenceTransformer usando
    # a constante MODELO_EMBEDDING.

    raise NotImplementedError(
        "Carregue o modelo"
    )

    # Depois de preencher o TODO 5, remova o raise acima
    # e descomente o restante desta função.

    # collection = criar_colecao(
    #     recriar=RECRIAR_COLECAO
    # )

    # if RECRIAR_COLECAO or collection.count() == 0:
    #     indexar_chunks(collection, modelo, chunks)
    # else:
    #     print(
    #         "Coleção persistente reutilizada. "
    #         f"Registros: {collection.count()}"
    #     )

    # while True:
    #     pergunta = input(
    #         "\nDigite sua pergunta ou 'sair': "
    #     ).strip()

    #     if pergunta.lower() == "sair":
    #         break

    #     if not pergunta:
    #         print("Digite uma pergunta válida.")
    #         continue

    #     if MODO_BUSCA == "mmr":
    #         resultados = buscar_mmr(
    #             collection,
    #             modelo,
    #             pergunta,
    #             k=TOP_K,
    #             fetch_k=FETCH_K_MMR,
    #             lambda_mult=LAMBDA_MMR,
    #         )
    #     else:
    #         resultados = buscar(
    #             collection,
    #             modelo,
    #             pergunta,
    #             k=TOP_K,
    #         )

    #     imprimir_resultados(resultados)


if __name__ == "__main__":
    main()