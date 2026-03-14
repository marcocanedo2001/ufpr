import subprocess

entradas = (
    "Matematica\n8\n7\n9\n"
    "Historia\n6\n5\n7\n"
    "Ciencias\n9\n8\n10\n"
)

print("Entradas do teste:")
print(entradas)

resultado = subprocess.run(
    ["python3", "dicionario7.py"],
    input=entradas,
    capture_output=True,
    text=True
)

print("Saida do programa:")
print(resultado.stdout)
