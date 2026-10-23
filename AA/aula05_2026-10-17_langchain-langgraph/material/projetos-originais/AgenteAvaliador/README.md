# Agente avaliador de comentários

Autor: Marco Antônio Canedo.

O agente consulta uma API de avaliações e classifica cada comentário como `positivo` ou `negativo`.

O arquivo principal é `agente_avaliacoes.py`. A classificação usa uma chain com `ChatPromptTemplate`, `ChatOllama` e `StrOutputParser`. O modelo é o `qwen2.5:3b`, executado localmente pelo Ollama, com temperatura zero.

## Preparação e execução

Requer Python 3.11, Ollama instalado e acesso à API pública de avaliações.

Na pasta do projeto, crie um ambiente para instalar as dependências. Os comandos abaixo usam Conda, disponível no Miniconda ou Anaconda:

```powershell
conda create -n avaliador python=3.11 pip -y
conda activate avaliador
conda env config vars set PYTHONNOUSERSITE=1
conda deactivate
conda activate avaliador
python -m pip install -r requirements.txt
```

Com o Ollama instalado e seu comando disponível no terminal:

```powershell
ollama pull qwen2.5:3b
ollama list
```

Mantenha o serviço Ollama ativo em `http://localhost:11434`. Se ainda não estiver iniciado, execute `ollama serve` em outro terminal. Na instalação Windows, o aplicativo pode já manter esse serviço ativo.

Execute o agente:

```powershell
python agente_avaliacoes.py
```

A execução começa na função `main`. Importar o arquivo em outro programa não inicia consultas nem classificações.

## Política e saída

A classificação considera a experiência geral relatada pelo cliente, seguindo estas regras:

1. Contar cada aspecto mencionado uma vez.
2. Se houver apenas um aspecto, seguir o sentimento desse aspecto.
3. Se houver vários, seguir a maioria dos aspectos positivos ou negativos.
4. Em empate, priorizar o produto e, depois, o atendimento.
5. Se esses critérios não resolverem o empate, retornar `negativo`.

A resposta deve conter somente `positivo` ou `negativo`. A validação converte o texto para minúsculas, remove espaços das extremidades e rejeita outros valores. O parser extrai o texto da resposta; a classificação pode estar errada mesmo quando o rótulo é válido.

Os resultados aparecem no terminal em JSON, com os campos `id`, `texto`, `esperado`, `saida_bruta`, `previsto` e `erro`. O texto original é preservado. Quando não há identificador na origem, o programa usa a posição do item na página. Nas avaliações da API, o campo `esperado` fica nulo, pois não há classificação de referência revisada.

Se uma avaliação tiver descrição inválida, falha de comunicação ou resposta fora das opções permitidas, o programa registra o erro, deixa a previsão nula e continua com as demais. Falhas na coleta são informadas e encerram a execução. O código de saída é zero no sucesso e um quando há falha na coleta ou em algum item.

## API e rede

Fonte: `https://apis.codante.io/api/reviews-api/reviews`. A coleta usa timeout de 20 segundos e verifica o status HTTP. Consulta somente **a página retornada por essa URL**, sem percorrer automaticamente a paginação e sem repetição automática.

A consulta à API usa o proxy configurado no ambiente. A conexão com o Ollama é direta, em `localhost`, sem passar pelo proxy. Se a rede exigir autenticação, o proxy deve estar configurado antes da execução.

## Testes

Testes de contratos e falhas, sem API nem Ollama:

```powershell
python -m unittest -v test_agente_avaliacoes
```

Teste com o modelo real, sem consultar a API:

```powershell
python test_agente_avaliacoes.py --modelo-real
```

O teste com o modelo usa dez comentários: seis de desenvolvimento e quatro complementares. Os rótulos esperados foram definidos antes da execução. O relatório mostra a resposta original, a previsão validada e os erros. Quando há divergência, o teste retorna código de saída um.

## Resultados observados

Os quatro testes de contratos passaram. No teste com `qwen2.5:3b`, foram oito classificações corretas em dez e nenhuma falha de formato ou comunicação: seis de seis nos comentários de desenvolvimento e duas de quatro nos complementares.

O modelo errou estes dois comentários:

| Comentário | Esperado | Modelo |
|---|---|---|
| Não tive nenhum problema com o equipamento. | positivo | negativo |
| O equipamento funciona perfeitamente, mas a entrega demorou demais. | positivo, pela prioridade do produto no empate | negativo |

Na execução da API, foram processadas dez avaliações sem falhas de formato ou comunicação. Como não houve revisão humana independente dos rótulos dessas avaliações, não foi calculada acurácia para os dados da API. Os resultados acima se referem às rodadas realizadas e podem variar em novas execuções.

## Limitações

A amostra é pequena, e os seis comentários de desenvolvimento já foram usados nos ajustes do prompt. Os testes não constituem uma avaliação humana independente nem permitem concluir que o mesmo desempenho ocorrerá em outros comentários.

A política ainda precisa de critérios mais precisos para atributos do mesmo produto, como som, conforto e durabilidade. Comentários neutros e sentimentos opostos dentro de um único aspecto também não têm tratamento específico.

Os resultados são exibidos no terminal e não são salvos em arquivo. O desafio adicional de gerar respostas aos comentários não foi implementado.
