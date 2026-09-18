# Aula 04 — Engenharia de contexto para RAG

O notebook original [`genai.ipynb`](genai.ipynb) indexa PDFs locais com
ChromaDB e o modelo multilíngue
`paraphrase-multilingual-MiniLM-L12-v2`.

Para estudar o conteúdo e realizar a atividade, use preferencialmente
[`genai_didatico.ipynb`](genai_didatico.ipynb). Essa versão preserva o
algoritmo da professora, divide o código em etapas comentadas e inclui um
roteiro de coleta dos resultados pedidos em `Atividade.pdf`.
Ao final, ele gera um relatório preenchido em Markdown e HTML; o HTML pode ser
enviado diretamente ou impresso como PDF pelo navegador.

## Preparação

No diretório desta aula:

```bash
source .venv/bin/activate
jupyter lab
```

Abra `genai_didatico.ipynb` e selecione o kernel **Python (aula04)**. Execute
as células na ordem apresentada. Na primeira execução o modelo de embeddings
é baixado da Hugging Face; por isso é necessária conexão com a internet.

O notebook didático pode ser regenerado após alterações no original com:

```bash
python scripts/gerar_notebook_didatico.py
```

## Dados e artefatos

- Os PDFs originais usados na aula já estão em `documentos/`: o regulamento de
  estágio, o PPC do curso e a ficha da disciplina CI1218. Coloque nessa pasta
  outros PDFs apenas se quiser incluí-los na indexação.
- O índice vetorial é criado em `chroma_db/` e é ignorado pelo Git.
- Para recriar o índice, mantenha `RECRIAR_COLECAO = True` no notebook; depois
  da primeira indexação, altere para `False` para reutilizá-lo.
