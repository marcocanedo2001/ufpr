# MBA IA Generativa - Exercicios de Python

Este repositorio contem exercicios introdutorios de Python desenvolvidos na primeira aula.

## Exercicios

1. `PYAI/aula01/ex01_imc.py` - calculo de IMC a partir de peso e altura.
2. `PYAI/aula01/ex02_circulo.py` - calculo de perimetro e area de um circulo.
3. `PYAI/aula01/ex03_bhaskara.py` - calculo das raizes reais de uma equacao de segundo grau.

## Como executar

Ao entrar em `PYAI/aula01`, o ambiente Conda `pyaula1` pode ser ativado automaticamente pelo `zsh`.

Ativacao manual (se necessario):

```bash
conda activate pyaula1
```

Se o ambiente ainda nao existir:

```bash
conda env create -f environment.yml
```

Depois disso, execute com Python 3 no terminal:

```bash
python3 PYAI/aula01/ex01_imc.py
python3 PYAI/aula01/ex02_circulo.py
python3 PYAI/aula01/ex03_bhaskara.py
```

## Trabalho em equipe

- Crie uma branch por tarefa, por exemplo: `feat/aula01-ex01`.
- Abra Pull Request para revisao antes de mergear na `main`.
- Siga o guia em `CONTRIBUTING.md`.

Teste de commit automatizado em 2026-03-08.
