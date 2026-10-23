# Ambiente de Agentes e Automações

Segue o padrão do ambiente `dsllm`: arquivo Conda na disciplina, Python 3.11 e kernel próprio. O ambiente `aa` é separado para evitar alterações nas dependências das aulas anteriores.

Na raiz do repositório, no terminal do Miniconda:

```powershell
conda env create -f AA/environment.yml
conda activate aa
python -m ipykernel install --user --name aa --display-name "Python (AA)"
cd AA/aula05_2026-10-17_langchain-langgraph
python verificar_ambiente.py
python -m unittest discover -s tests -v
jupyter lab
```

Selecione **Python (AA)** no Jupyter. Se o ambiente já existir, use `conda env update -n aa -f AA/environment.yml` a partir da raiz. O comando não remove outros ambientes. Os comandos acima preparam o computador em que forem executados; a edição destes arquivos não instala nada automaticamente no seu Windows.

Alternativa sem Conda: crie um venv com Python 3.11, ative-o e instale o `requirements.txt` da aula. Registre o kernel desse venv com o mesmo comando de ipykernel.

Os três primeiros exercícios podem ser feitos com dados sintéticos e modelo simulado. Para chamadas reais locais, instale e inicie o Ollama no computador e disponibilize o modelo escolhido. `langchain-ollama` é a integração Python; não instala o servidor nem os pesos. O exemplo de aula usa `llama3.2:1b`, cuja disponibilidade e desempenho devem ser verificados no seu ambiente. Nenhum download de pesos é automático nestes notebooks.

Se optar pelo exemplo remoto Groq do professor, configure a variável de ambiente no seu computador. Não publique chaves, `.env` ou respostas que contenham dados pessoais. Nenhuma chave é necessária para os exercícios offline.

A versão de LangGraph fixada é a usada na verificação do exemplo desta preparação. Os demais intervalos facilitam a criação do ambiente; após instalá-lo, registre as versões efetivas com `python -m pip freeze > versoes-locais.txt`. A solução completa Conda no Windows e a inferência com Ollama ainda precisam de validação no computador do aluno.
