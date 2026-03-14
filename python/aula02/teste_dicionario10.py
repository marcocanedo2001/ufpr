import subprocess

entradas = "Python e divertido. Python e simples, e Python ajuda muito!\n"

print("Entradas do teste:")
print(entradas)

resultado = subprocess.run(
    ["python3", "dicionario10.py"],
    input=entradas,
    capture_output=True,
    text=True
)

print("Saida do programa:")
print(resultado.stdout)
