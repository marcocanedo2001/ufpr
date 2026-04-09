# MBA IA Generativa - Python Aula 02

Material de apoio e exercicios da segunda aula de Python.

## Objetivo

Praticar estruturas de dados basicas em Python com scripts curtos, exercicios interativos e testes simples.

## Conteudo

- `lista*.py`: exercicios com listas, iteracao, busca, ordenacao e matrizes.
- `tupla*.py` e `tupla*.ipynb`: exemplos de tuplas, retornos multiplos e conversao de unidades.
- `dicionario*.py`: exercicios com cadastro, consulta, relatorios e recomendacao usando dicionarios.
- `teste_lista7.py`: teste automatizado para validar a saida de `lista7.py`.
- `tupla11.py`: sistema de funcionarios modelado com tuplas e funcoes de alta ordem.
- `environment.yml`: definicao do ambiente Conda da aula.

## Ambiente Conda

Este projeto usa o ambiente Conda `pyaula2`.

Neste computador, terminais `zsh` abertos dentro de `aula02` ativam `pyaula2` automaticamente.

Criar o ambiente do zero:

```bash
conda env create -f environment.yml
```

Ativar o ambiente:

```bash
conda activate pyaula2
```

Atualizar as dependencias do ambiente:

```bash
conda env update -n pyaula2 -f environment.yml --prune
```

## Como executar

Rodar um exercicio qualquer:

```bash
python lista1.py
```

Rodar o exercicio de tuplas 11:

```bash
python tupla11.py
```

Rodar o teste automatizado:

```bash
python teste_lista7.py
```

## Observacoes

- Os scripts usam apenas a biblioteca padrao do Python.
- No VS Code, o workspace aponta para o interpretador do `pyaula2`.
