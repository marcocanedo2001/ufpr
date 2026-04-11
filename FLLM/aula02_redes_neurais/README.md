# Ambiente da aula

O ambiente Conda desta aula usa o nome `FLLMS02`.

## Criar o ambiente

```bash
~/miniconda3/condabin/conda env create -f environment.yml
```

## Ativar

```bash
conda activate FLLMS02
```

Se o `conda` não estiver no `PATH`, use:

```bash
source ~/miniconda3/etc/profile.d/conda.sh
conda activate FLLMS02
```

## Registrar kernel no Jupyter

```bash
python -m ipykernel install --user --name FLLMS02 --display-name "Python (FLLMS02)"
```

## Abrir o Jupyter

```bash
jupyter lab
```
