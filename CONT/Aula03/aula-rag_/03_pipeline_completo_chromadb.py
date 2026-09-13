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

# Modos disponíveis: "similaridade" ou "mmr".
MODO_BUSCA = "similaridade"

# No MMR, primeiro recuperamos um conjunto maior de candidatos.
FETCH_K_MMR = 12

# Próximo de 1: prioriza relevância.
# Menor: aumenta a diversidade.
LAMBDA_MMR = 0.6

# Na primeira execução, deixe True.
# Depois, altere para False para demonstrar persistência.
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
# CHUNKING
# ============================================================

def gerar_chunks(
    texto: str,
    tamanho: int = TAMANHO_CHUNK,
    overlap: int = OVERLAP_CHUNK,
) -> list[str]:
    if tamanho <= 0:
        raise ValueError(
            "O tamanho do chunk deve ser maior que zero."
        )

    if overlap < 0:
        raise ValueError(
            "O overlap não pode ser negativo."
        )

    if overlap >= tamanho:
        raise ValueError(
            "O overlap deve ser menor que o tamanho."
        )

    chunks = []
    inicio = 0
    passo = tamanho - overlap

    while inicio < len(texto):
        fim = min(inicio + tamanho, len(texto))
        chunk = texto[inicio:fim].strip()

        if chunk:
            chunks.append(chunk)

        inicio += passo

    return chunks


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
# BANCO VETORIAL
# ============================================================

def criar_colecao(recriar: bool):
    PASTA_CHROMA.mkdir(parents=True, exist_ok=True)

    client = chromadb.PersistentClient(
        path=str(PASTA_CHROMA)
    )

    if recriar:
        try:
            client.delete_collection(NOME_COLECAO)
            print(
                f"Coleção anterior removida: {NOME_COLECAO}"
            )
        except Exception:
            # A coleção ainda pode não existir.
            pass

    collection = client.get_or_create_collection(
        name=NOME_COLECAO,
        configuration={
            "hnsw": {
                "space": "cosine",
            }
        },
    )

    return collection


# ============================================================
# EMBEDDINGS E INDEXAÇÃO
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

        embeddings = modelo.encode(
            textos,
            batch_size=TAMANHO_LOTE,
            normalize_embeddings=True,
            show_progress_bar=False,
        )

        collection.upsert(
            ids=[chunk["id"] for chunk in lote],
            embeddings=embeddings.tolist(),
            documents=textos,
            metadatas=[
                {
                    "arquivo": chunk["arquivo"],
                    "pagina": chunk["pagina"],
                    "numero_chunk": chunk["numero_chunk"],
                    "tamanho_caracteres": len(
                        chunk["texto"]
                    ),
                }
                for chunk in lote
            ],
        )

        print(f"Indexados: {fim}/{total}")

    tempo = perf_counter() - inicio_total

    print(f"Indexação concluída em {tempo:.2f} s.")
    print(f"Registros na coleção: {collection.count()}")


# ============================================================
# BUSCA VETORIAL
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

    total_registros = collection.count()

    if total_registros == 0:
        raise RuntimeError("A coleção está vazia.")

    k_real = min(k, total_registros)

    embedding_pergunta = modelo.encode(
        pergunta,
        normalize_embeddings=True,
    ).tolist()

    inicio = perf_counter()

    resultados = collection.query(
        query_embeddings=[embedding_pergunta],
        n_results=k_real,
        include=[
            "documents",
            "metadatas",
            "distances",
        ],
    )

    resultados["latencia_ms"] = (
        perf_counter() - inicio
    ) * 1000

    resultados["pergunta"] = pergunta
    resultados["metodo"] = "similaridade"

    return resultados


# ============================================================
# MAXIMAL MARGINAL RELEVANCE
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
    resultados equilibrando relevância para a pergunta e
    diversidade em relação aos chunks já escolhidos.
    """

    pergunta = pergunta.strip()

    if not pergunta:
        raise ValueError(
            "A pergunta não pode estar vazia."
        )

    if k <= 0:
        raise ValueError(
            "k deve ser maior que zero."
        )

    if fetch_k < k:
        raise ValueError(
            "fetch_k deve ser maior ou igual a k."
        )

    if not 0 <= lambda_mult <= 1:
        raise ValueError(
            "lambda_mult deve estar entre 0 e 1."
        )

    total_registros = collection.count()

    if total_registros == 0:
        raise RuntimeError(
            "A coleção está vazia."
        )

    k_real = min(k, total_registros)
    fetch_k_real = min(
        max(fetch_k, k_real),
        total_registros,
    )

    embedding_pergunta = modelo.encode(
        pergunta,
        normalize_embeddings=True,
    )

    inicio = perf_counter()

    candidatos = collection.query(
        query_embeddings=[
            embedding_pergunta.tolist()
        ],
        n_results=fetch_k_real,
        include=[
            "documents",
            "metadatas",
            "distances",
            "embeddings",
        ],
    )

    ids = candidatos["ids"][0]
    documentos = candidatos["documents"][0]
    metadados = candidatos["metadatas"][0]
    embeddings = np.asarray(
        candidatos["embeddings"][0],
        dtype=np.float32,
    )

    # Os embeddings foram normalizados durante a indexação.
    # O produto escalar corresponde à similaridade de cosseno.
    relevancias = embeddings @ embedding_pergunta

    selecionados = [
        int(np.argmax(relevancias))
    ]

    while (
        len(selecionados) < k_real
        and len(selecionados) < len(ids)
    ):
        melhor_indice = None
        melhor_score = float("-inf")

        for indice in range(len(ids)):
            if indice in selecionados:
                continue

            redundancias = (
                embeddings[selecionados]
                @ embeddings[indice]
            )

            maior_redundancia = float(
                np.max(redundancias)
            )

            score_mmr = (
                lambda_mult
                * float(relevancias[indice])
                - (1 - lambda_mult)
                * maior_redundancia
            )

            if score_mmr > melhor_score:
                melhor_score = score_mmr
                melhor_indice = indice

        if melhor_indice is None:
            break

        selecionados.append(melhor_indice)

    latencia_ms = (
        perf_counter() - inicio
    ) * 1000

    similaridades_selecionadas = [
        float(relevancias[indice])
        for indice in selecionados
    ]

    # Mantém o formato usado por imprimir_resultados().
    resultados = {
        "ids": [[ids[indice] for indice in selecionados]],
        "documents": [[
            documentos[indice]
            for indice in selecionados
        ]],
        "metadatas": [[
            metadados[indice]
            for indice in selecionados
        ]],
        "distances": [[
            1 - similaridade
            for similaridade
            in similaridades_selecionadas
        ]],
        "latencia_ms": latencia_ms,
        "pergunta": pergunta,
        "metodo": "MMR",
        "lambda_mmr": lambda_mult,
        "fetch_k": fetch_k_real,
    }

    return resultados


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
        f"Método: "
        f"{resultados.get('metodo', 'similaridade')}"
    )
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
        # Para a métrica de cosseno usada pelo Chroma:
        # distância = 1 - similaridade de cosseno.
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
    try:
        print("1. Carregando PDFs...")
        paginas = carregar_pdfs(PASTA_DOCUMENTOS)
        print(f"Páginas com texto: {len(paginas)}")

        print("\n2. Gerando chunks...")
        chunks = preparar_chunks(paginas)
        print(f"Total de chunks: {len(chunks)}")

        print("\n3. Carregando o modelo de embeddings...")
        modelo = SentenceTransformer(MODELO_EMBEDDING)

        print(f"Modelo: {MODELO_EMBEDDING}")
        print(
            "Dimensão dos embeddings: "
            f"{modelo.get_sentence_embedding_dimension()}"
        )

        print("\n4. Preparando a coleção...")
        collection = criar_colecao(
            recriar=RECRIAR_COLECAO
        )

        if RECRIAR_COLECAO or collection.count() == 0:
            print("\n5. Indexando os chunks...")
            indexar_chunks(
                collection,
                modelo,
                chunks,
            )
        else:
            print(
                "\nColeção persistente reutilizada. "
                f"Registros: {collection.count()}"
            )

        print("\n6. Busca interativa")

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

            if MODO_BUSCA == "mmr":
                resultados = buscar_mmr(
                    collection,
                    modelo,
                    pergunta,
                    k=TOP_K,
                    fetch_k=FETCH_K_MMR,
                    lambda_mult=LAMBDA_MMR,
                )
            else:
                resultados = buscar(
                    collection,
                    modelo,
                    pergunta,
                    k=TOP_K,
                )

            imprimir_resultados(resultados)

    except KeyboardInterrupt:
        print("\nPrograma interrompido.")

    except (
        FileNotFoundError,
        ValueError,
        RuntimeError,
    ) as erro:
        print(f"\nErro: {erro}")

    except Exception as erro:
        print(
            "\nErro inesperado: "
            f"{type(erro).__name__}: {erro}"
        )


if __name__ == "__main__":
    main()