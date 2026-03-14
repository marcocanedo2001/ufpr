import subprocess

print("Entradas do teste:")
print("O programa usa um grafo fixo e executa operacoes de exemplo dentro do arquivo.")

resultado = subprocess.run(
    ["python3", "dicionario12.py"],
    capture_output=True,
    text=True
)

print("Saida do programa:")
print(resultado.stdout)
