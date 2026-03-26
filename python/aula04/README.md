# MBA IA Generativa - Python Aula 04

Material de apoio e organizacao da quarta aula de Python.

## Objetivo da aula

Consolidar os conceitos de orientacao a objetos parte 2, mantendo a estrutura do repositorio pronta para novos exemplos, exercicios e exploracoes praticas.

## Topicos cobertos

- Orientacao a objetos parte 2 com base no material `OO Parte 2.pdf`.
- Continuidade dos conceitos de classes e objetos introduzidos na aula anterior.
- Reforco de modelagem orientada a objetos com foco em reutilizacao e organizacao do codigo.
- Espaco preparado para exemplos futuros da aula conforme o conteudo for sendo praticado.

## Material principal

- `OO Parte 2.pdf`: slides e conteudo de referencia da aula.

## Organizacao atual da pasta

A aula 04 agora inclui o pacote `src/` com as classes reaproveitadas da aula 03:

- `src/universidade/pessoa.py`
- `src/universidade/disciplina.py`
- `src/universidade/conteudo_ministrado.py`
- `src/main.py` com um exemplo executavel

Novos scripts, modulos ou notebooks podem ser adicionados diretamente em `python/aula04/` conforme a aula evoluir.

## Ambiente Conda da aula

Este projeto usa um ambiente Conda nomeado `pyaula4`.

Para criar o ambiente do zero com o arquivo `environment.yml`:

```bash
conda env create -f environment.yml
```

Para ativar manualmente:

```bash
conda activate pyaula4
```

Para sincronizar as dependencias caso o ambiente ja exista:

```bash
conda env update -n pyaula4 -f environment.yml --prune
```

## Ativacao automatica

Ao abrir a pasta `aula04` no VS Code, o interpretador configurado para o workspace sera o do ambiente `pyaula4`.

Ao abrir um terminal `zsh` ja dentro de `python/aula04/`, o ambiente `pyaula4` sera ativado automaticamente pela configuracao do shell.

## Como trabalhar na aula

Entrar na pasta:

```bash
cd /home/marco/mba_genai/python/aula04
```

Confirmar o ambiente ativo:

```bash
echo $CONDA_DEFAULT_ENV
```

Executar futuros scripts da aula:

```bash
python nome_do_script.py
```

## Observacoes

- O ambiente da aula herda a base da aula 03 e inclui `numpy`.
- O material principal desta etapa esta concentrado no PDF da aula.
