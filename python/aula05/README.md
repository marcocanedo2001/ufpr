# MBA IA Generativa - Python Aula 05

Material de apoio e organizacao da quinta aula de Python, com foco em criacao e consumo de APIs.

## Objetivo da aula

Construir uma base pratica para:

- consumir APIs HTTP com Python;
- criar APIs locais com FastAPI;
- testar endpoints e documentacao automatica;
- aplicar metodos HTTP corretos e tratamento de erros.

## Material principal

- `../Criação de APIs.pdf`: slides e roteiro da aula.

## Topicos cobertos

- Conceito de API (Application Programming Interface).
- Requisicoes HTTP do tipo GET e uso de query params.
- Consumo de APIs externas com `requests` (exemplo com Open-Meteo).
- Criacao de servidor com FastAPI.
- Endpoints com Query Params e Path Params.
- Type hints para validacao de parametros.
- Documentacao automatica em `/docs`.
- Metodos HTTP (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`) e idempotencia.
- Tratamento de erros com `HTTPException`.
- Introducao a chamadas assincronas com `async`.
- Orquestracao de APIs (API chamando outras APIs).

## Ambiente da aula

Esta pasta usa ambiente virtual Python local `pyaula05`.

Ao entrar em `python/aula05` no terminal `zsh`, o ambiente e ativado automaticamente.

Ativacao manual (se necessario):

```bash
source pyaula05/bin/activate
```

Instalacao de dependencias usadas no material:

```bash
pip install fastapi "uvicorn[standard]" requests
```

## Fluxo pratico da aula

1. Criar um cliente (`consumidor.py`) para chamar APIs externas via `requests`.
2. Buscar latitude/longitude por cidade na API de geocoding.
3. Chamar previsao/tempo atual com latitude e longitude obtidas.
4. Criar um servidor (`servidor.py`) com FastAPI e endpoints simples.
5. Subir servidor local com:

```bash
fastapi dev servidor.py
```

6. Testar no navegador:

- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/docs`

## Exemplos de evolucao dos endpoints

- Endpoint de saudacao.
- Endpoint de hora atual.
- Endpoint para verificacao de CPF com query param.
- Endpoint para verificacao de CPF com path param.
- Endpoint de cadastro de pessoa com `POST`.
- Endpoint de consulta de pessoas com `GET`.

## Boas praticas reforcadas na aula

- Usar cada metodo HTTP para a finalidade correta.
- Evitar alterar estado do sistema via `GET`.
- Validar e documentar parametros com tipagem e anotacoes.
- Retornar erros de forma padrao com `HTTPException`.
- Testar continuamente via `/docs` durante o desenvolvimento.
- Manter servico em modo local durante estudos (`fastapi dev`).

## Exercicios propostos no material

1. Criar scripts Python para consumir os endpoints construidos na aula.
2. Subir o servico FastAPI sem `dev` em rede local para testes controlados.
3. Criar endpoint que recebe nome da cidade e orquestra chamadas ao Open-Meteo.
4. Retornar dados consolidados (por exemplo: coordenadas + temperatura atual).

## Observacoes

- O PDF inclui orientacoes com Conda; nesta pasta usamos `venv` (`pyaula05`).
- O conteudo pode ser expandido conforme novos scripts e exemplos forem adicionados.
