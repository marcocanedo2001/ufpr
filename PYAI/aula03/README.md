# MBA IA Generativa - Python Aula 03

Material de apoio e organizacao da terceira aula de Python.

## Objetivo da aula

Preparar a estrutura da aula para os temas de modularizacao e orientacao a objetos parte 1, mantendo o padrao adotado no repositorio.

## Topicos cobertos

- Modularizacao em Python com modulos e importacoes.
- Organizacao de funcoes relacionadas em arquivos reutilizaveis.
- Introducao a classes e objetos.
- Convencoes de nomes para arquivos e classes.
- Atributos, inicializador, encapsulamento basico com `property`.

## Organizacao sugerida

Os proximos arquivos da aula devem ser adicionados diretamente em `python/aula03/`.
Se a aula crescer, subpastas tematicas simples podem ser criadas, mas nao ha uso de `src/` nesta estrutura.

## Ambiente Conda da aula

Este projeto usa um ambiente Conda nomeado `pyaula3`.

Para criar o ambiente do zero com o arquivo `environment.yml`:

```bash
conda env create -f environment.yml
```

Para ativar:

```bash
conda activate pyaula3
```

Para desativar:

```bash
conda deactivate
```

Se o ambiente `pyaula3` ja existir e voce quiser sincronizar as dependencias:

```bash
conda env update -n pyaula3 -f environment.yml --prune
```

## Convencoes para os proximos arquivos

- Modulos e scripts em `snake_case.py`.
- Classes em `UpperCamelCase`.
- Um arquivo por classe quando fizer sentido didatico.

## Exemplos de nomes esperados

- `main.py`
- `fibonacci.py`
- `pessoa.py`
- `professor.py`
- `sala_aula.py`

Esses nomes sao apenas referencias para a organizacao futura da aula. Nenhum codigo inicial foi adicionado nesta etapa.
