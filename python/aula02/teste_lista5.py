import subprocess

entradas = "7\n8\n5\n10\n-1\n"

print("Entradas do teste:")
print(entradas)

resultado = subprocess.run(
    ["python3", "lista5.py"],
    input=entradas,
    capture_output=True,
    text=True
)

print("Saida do programa:")
print(resultado.stdout)
