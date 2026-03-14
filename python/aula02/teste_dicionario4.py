import subprocess

entradas = "mesa\n"

print("Entradas do teste:")
print(entradas)

resultado = subprocess.run(
    ["python3", "dicionario4.py"],
    input=entradas,
    capture_output=True,
    text=True
)

print("Saida do programa:")
print(resultado.stdout)
