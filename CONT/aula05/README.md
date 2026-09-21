# Aula 05 — RAG Híbrido

Este diretório contém uma versão local do notebook da aula. O original foi
feito para Google Colab; a cópia `RAG_Hibrido_aula_3_local.ipynb` usa caminhos
relativos a este diretório.

## Preparação

No Linux/macOS, execute:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m ipykernel install --user --name aula05-rag-hibrido --display-name "Python (aula05 RAG híbrido)"
.venv/bin/jupyter lab
```

Em Ubuntu/Debian, se o primeiro comando informar que `ensurepip` não está
disponível, instale antes o componente do Python do sistema:

```bash
sudo apt-get update && sudo apt-get install -y python3.12-venv
```

No Jupyter, selecione o kernel **Python (aula05 RAG híbrido)** e abra
`RAG_Hibrido_aula_3_local.ipynb`.

### Compilador para execução com Triton

Se a geração na GPU falhar com `Failed to find C compiler`, instale as
ferramentas de compilação e os cabeçalhos da versão de Python do kernel.
Para o ambiente Python 3.12 desta aula, em Ubuntu/Debian, execute no terminal:

```bash
sudo apt-get update
sudo apt-get install build-essential python3.12-dev
```

O Triton pode compilar componentes nativos durante a execução. `build-essential`
fornece compiladores e ferramentas; `python3.12-dev` fornece, entre outros
arquivos, `Python.h`. Essas dependências do sistema não são instaladas pelo
`pip install -r requirements.txt`.

Depois, reinicie o kernel e execute novamente as células necessárias à geração.
Definir a variável `CC` só ajuda se já houver um compilador instalado; a variável
não instala o compilador. Se o pré-processamento retornar
`origem = fallback_pergunta_original`, confira `diagnostico.erro` para verificar
se ainda há falha de execução.

## Documentos

O notebook original recebia os PDFs por upload no Colab; eles não estão
incorporados ao arquivo `.ipynb`. Coloque em `documentos/` o corpus da aula:

- `ci1218.pdf` — ficha da disciplina Bancos de Dados;
- `PPC-do-Curso-de-Ciencia-da-Computação.pdf` — Projeto Pedagógico do Curso;
- `2024-regulamento-estagio.pdf` — regulamento de estágio.

O arquivo `genia_3.pdf` presente neste diretório é material de aula e não deve
substituir esse corpus; a versão local do notebook o exclui da indexação. O
Chroma persistirá o índice local em `chroma/` e o log será gravado em
`rag_hibrido_pre_pos_log.jsonl`.

## Modelo e recursos

O notebook baixa, na primeira execução, `Qwen/Qwen2.5-1.5B-Instruct` e o
modelo de embeddings da Hugging Face. É necessária conexão com a internet e
espaço em disco; GPU é recomendada. Em CPU o fluxo funciona, mas a geração
será consideravelmente mais lenta.
