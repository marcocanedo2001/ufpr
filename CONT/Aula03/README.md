# Aula 03 — RAG

## Estrutura

- `aula-rag_/01_visualizar_embeddings.py`: visualização dos embeddings.
- `aula-rag_/02_pipeline_incompleto.py`: pipeline local com ChromaDB para completar em aula.
- `aula-rag_/03_pipeline_completo_chromadb.py`: pipeline local completo com persistência.
- `aula-rag_/03_pipeline_completo_pinecone.py`: pipeline usando Pinecone; requer `PINECONE_API_KEY`.
- `aula-rag_/data/documentos/`: PDFs usados nos experimentos.
- `aula-rag_/figuras/`: gráficos gerados.
- `aula-rag_/chroma_db/`: banco local gerado pelo ChromaDB.

## Preparação

```bash
source .venv/bin/activate
python -m pip install -r aula-rag_/requirements.txt
```

Execute os scripts a partir de `aula-rag_`, pois os caminhos dos dados são relativos a essa pasta:

```bash
cd aula-rag_
python 01_visualizar_embeddings.py
python 03_pipeline_completo_chromadb.py
```

Para o experimento com Pinecone, copie `.env.example` para `.env` e preencha a chave:

```bash
cp .env.example .env
python 03_pipeline_completo_pinecone.py
```
