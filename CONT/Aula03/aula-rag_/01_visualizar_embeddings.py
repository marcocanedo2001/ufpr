from pathlib import Path

import matplotlib.pyplot as plt
from sentence_transformers import SentenceTransformer
from sklearn.decomposition import PCA


MODELO = (
    "sentence-transformers/"
    "paraphrase-multilingual-MiniLM-L12-v2"
)

PASTA_SAIDA = Path("figuras")
ARQUIVO_SAIDA = PASTA_SAIDA / "embeddings_pca.png"


def main() -> None:
    grupos = {
        "Banco de dados": [
            "consulta SQL",
            "linguagem de consulta",
            "otimização de consultas",
            "processamento de consultas",
        ],
        "Estágio": [
            "estágio obrigatório",
            "carga horária do estágio",
            "supervisão de estágio",
            "relatório de estágio",
        ],
        "Computação paralela": [
            "processamento paralelo",
            "execução com múltiplas threads",
            "programação paralela",
            "computação de alto desempenho",
        ],
    }

    frases = [
        frase
        for frases_do_grupo in grupos.values()
        for frase in frases_do_grupo
    ]

    print("Carregando o modelo...")
    modelo = SentenceTransformer(MODELO)

    print("Gerando embeddings...")
    embeddings = modelo.encode(
        frases,
        normalize_embeddings=True,
        show_progress_bar=True,
    )

    print(f"Formato da matriz: {embeddings.shape}")
    print(f"Dimensões por embedding: {embeddings.shape[1]}")

    pca = PCA(n_components=2)
    embeddings_2d = pca.fit_transform(embeddings)

    variancia = pca.explained_variance_ratio_.sum()
    print(
        "Variância representada pelos dois componentes: "
        f"{variancia:.2%}"
    )

    fig, ax = plt.subplots(figsize=(11, 7))

    indice_inicial = 0

    for nome_grupo, frases_do_grupo in grupos.items():
        quantidade = len(frases_do_grupo)
        indice_final = indice_inicial + quantidade
        pontos = embeddings_2d[indice_inicial:indice_final]

        # Cada chamada recebe automaticamente uma cor do Matplotlib.
        ax.scatter(
            pontos[:, 0],
            pontos[:, 1],
            s=85,
            label=nome_grupo,
        )

        for frase, (x, y) in zip(frases_do_grupo, pontos):
            ax.annotate(
                frase,
                xy=(x, y),
                xytext=(6, 6),
                textcoords="offset points",
                fontsize=9,
            )

        indice_inicial = indice_final

    ax.set_title("Projeção 2D dos embeddings com PCA")
    ax.set_xlabel("Primeiro componente principal")
    ax.set_ylabel("Segundo componente principal")
    ax.grid(alpha=0.3)
    ax.legend()

    fig.tight_layout()

    PASTA_SAIDA.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        ARQUIVO_SAIDA,
        dpi=300,
        bbox_inches="tight",
    )

    print(f"Figura salva em: {ARQUIVO_SAIDA.resolve()}")
    plt.show()


if __name__ == "__main__":
    main()
