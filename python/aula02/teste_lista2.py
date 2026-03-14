import subprocess

entradas = "8\n3\n15\n1\n20\n7\n9\n"

print("Entradas do teste:")
print(entradas)

resultado = subprocess.run(
    ["python3", "lista2.py"],
    input=entradas,
    capture_output=True,
    text=True
)

print("Saida do programa:")
print(resultado.stdout)
