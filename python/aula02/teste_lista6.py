import subprocess

entradas = "5\n2\n5\n8\n2\n9\n8\n1\n-1\n"

print("Entradas do teste:")
print(entradas)

resultado = subprocess.run(
    ["python3", "lista6.py"],
    input=entradas,
    capture_output=True,
    text=True
)

print("Saida do programa:")
print(resultado.stdout)
