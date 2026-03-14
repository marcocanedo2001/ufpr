import subprocess

entradas = "Ana Maria\n"

print("Entradas do teste:")
print(entradas)

resultado = subprocess.run(
    ["python3", "dicionario2.py"],
    input=entradas,
    capture_output=True,
    text=True
)

print("Saida do programa:")
print(resultado.stdout)
