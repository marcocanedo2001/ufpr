# MBA IA Generativa - Python Aula 06

Material de apoio e organizacao inicial da sexta aula de Python.

## Objetivo da aula

Preparar a estrutura da aula 06 para receber exemplos, exercicios e exploracoes praticas, mantendo o mesmo estilo operacional adotado nas aulas recentes de `PYAI`.

## Material principal

- Material da aula ainda sera adicionado nesta pasta conforme o conteudo for definido.

## Organizacao atual da pasta

Esta pasta foi criada como scaffold base da aula e inclui:

- `README.md` com orientacoes de uso;
- `environment.yml` com o ambiente Conda da aula;
- `.vscode/` com a configuracao local do workspace.

Novos scripts, modulos ou notebooks podem ser adicionados diretamente em `PYAI/aula06/` conforme a aula evoluir.

## Ambiente Conda da aula

Este projeto usa um ambiente Conda nomeado `pyaula6`.

Para criar o ambiente do zero com o arquivo `environment.yml`:

```bash
conda env create -f environment.yml
```

Para ativar manualmente:

```bash
conda activate pyaula6
```

Para sincronizar as dependencias caso o ambiente ja exista:

```bash
conda env update -n pyaula6 -f environment.yml --prune
```

## Como trabalhar na aula

Entrar na pasta:

```bash
cd /home/marco/mba_genai/PYAI/aula06
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

- A aula 06 segue o mesmo estilo de ambiente e workspace usado nas aulas recentes de `PYAI`.
- Nenhum script de exemplo foi adicionado nesta etapa; a pasta esta pronta para receber o conteudo oficial quando ele for definido.
