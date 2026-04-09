import requests

# Define a cidade que sera enviada para o servidor local.
cidade = "Curitiba"

# Define a URL do endpoint local que orquestra as chamadas ao Open-Meteo.
url = f"http://127.0.0.1:8000/clima/{cidade}"

# Faz a chamada para o servidor FastAPI local.
response = requests.get(url, timeout=10)

# Interrompe a execucao caso o servidor retorne erro HTTP.
response.raise_for_status()

# Converte a resposta JSON para dicionario Python.
dados = response.json()

# Exibe um resumo amigavel do resultado consolidado.
print(f"Cidade encontrada: {dados['cidade_encontrada']} - {dados['pais']}")
print(f"Latitude: {dados['latitude']}, Longitude: {dados['longitude']}")
print(f"Temperatura atual: {dados['clima_atual']['temperature']}°C")
print(f"Vento: {dados['clima_atual']['windspeed']} km/h")
print(f"Horario da leitura: {dados['clima_atual']['time']}")
