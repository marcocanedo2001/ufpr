# Ambiente do workspace DSLLM

O ambiente `dsllm` reúne as dependências usadas nas aulas 02, 04 e 05: scraping,
PDF/LLM, visualização, inferência estatística e NLP. Ele usa Python 3.11 e o
modelo `en_core_web_sm` do spaCy necessário à aula 05.

## Criar ou atualizar

Com o Miniconda instalado, na raiz deste workspace:

```bash
conda env create -f environment.yml
```

Se o ambiente já existir, atualize-o com:

```bash
conda env update -n dsllm -f environment.yml --prune
```

## Usar no terminal e no Jupyter

```bash
conda activate dsllm
python -m ipykernel install --user --name dsllm --display-name "Python (DSLLM)"
jupyter lab
```

No Jupyter, selecione o kernel **Python (DSLLM)**. Para sair do ambiente:

```bash
conda deactivate
```

## Validação rápida

```bash
python -c "import bs4, chatlas, matplotlib, numpy, pandas, plotnine, pydantic, pypdf, requests, scipy, sklearn, selenium, spacy, statsmodels; from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer; spacy.load('en_core_web_sm'); print('DSLLM: ambiente pronto')"
```

O scraping com Selenium também requer um navegador Chromium/Chrome instalado no
sistema. Consulte `aula02/lessons/04_imoveis_selenium/docs/SELENIUM_VNC_PROVISIONING.md`
para a execução em ambiente VNC.
