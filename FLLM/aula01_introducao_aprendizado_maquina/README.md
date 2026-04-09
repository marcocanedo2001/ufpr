# Aula 01 - Introducao ao Aprendizado de Maquina

## Informacoes da aula

- Data: 20/03/2026
- Dia: Sexta-feira
- Disciplina: FLLM
- Professor: Luiz
- Tema: Introducao ao Aprendizado de Maquina

## Estrutura da aula

- `notebooks/` - notebooks para demonstracoes, analises e experimentos.
- `exercicios/` - codigos Python e atividades praticas.
- `datasets/` - arquivos de dados usados durante a aula.

## Ambiente local com Miniconda

1. Instale o Miniconda no WSL2:

   ```bash
   curl -L https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o /tmp/Miniconda3-latest-Linux-x86_64.sh
   bash /tmp/Miniconda3-latest-Linux-x86_64.sh -b -p "$HOME/miniconda3"
   "$HOME/miniconda3/bin/conda" init zsh
   ```

2. Feche e reabra o terminal `zsh`.

3. Na raiz deste subprojeto, crie o ambiente local isolado:

   ```bash
   conda env create --prefix ./.conda --file environment.yml
   ```

4. Ative o ambiente:

   ```bash
   conda activate ./.conda
   ```

5. Registre o kernel Jupyter dedicado:

   ```bash
   python -m ipykernel install --user --name aula01-intro-ml --display-name "Python (aula01-intro-ml)"
   ```

6. Abra o Jupyter Lab:

   ```bash
   jupyter lab
   ```

7. No notebook `notebooks/lab_metricas_ml_nlp_llm.ipynb`, selecione o kernel `Python (aula01-intro-ml)`.

## Manutencao do ambiente

- `environment.yml` e a fonte unica de verdade das dependencias do projeto.
- O ambiente usa uma wheel CPU-only do PyTorch para evitar baixar dependencias CUDA desnecessarias no WSL.
- Para atualizar um ambiente ja existente, use:

  ```bash
  conda env update --prefix ./.conda --file environment.yml --prune
  ```

- Nao e necessario executar `pip install` dentro do notebook.
