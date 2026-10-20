# Aula 03

Aplicacao Streamlit para Engenharia de Prompt usando `chatlas` com API
compativel com OpenAI via endpoint de Chat Completions.

## Ambiente

O ambiente Conda desta aula se chama `aula03` e usa Python 3.11.

Para recriar o ambiente:

```bash
conda create -n aula03 python=3.11 -y
conda activate aula03
pip install -r requirements.txt
```

No VS Code, esta pasta tem `.vscode/settings.json` apontando para:

```bash
/home/espinf/mamcsantos/miniconda3/envs/aula03/bin/python
```

Ao abrir um novo terminal interativo dentro desta pasta, o `.zshrc` ou `.bashrc` ja ativa automaticamente:

```bash
conda activate aula03
```

Se o terminal ja estava aberto, recarregue a configuracao conforme o shell:

```bash
source ~/.zshrc
# ou
source ~/.bashrc
```

Ou ative manualmente:

```bash
source /home/espinf/mamcsantos/miniconda3/etc/profile.d/conda.sh
conda activate aula03
```

## Instalar dependencias

```bash
pip install -r requirements.txt
```

## Variaveis de ambiente

Crie um arquivo `.env` nesta pasta com a chave da NVIDIA. Voce pode copiar o
modelo:

```bash
cp .env.example .env
```

Depois edite o `.env`:

```bash
NVIDIA_API_KEY=sua_chave_aqui
```

O arquivo `.env` nao deve ser enviado para o Git.

## Rodar o app

```bash
streamlit run app.py
```
