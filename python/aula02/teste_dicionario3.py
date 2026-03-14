import subprocess

entradas = (
    "Ana\n8\n"
    "Bruno\n6\n"
    "Carla\n10\n"
    "Daniel\n7\n"
)

print("Entradas do teste:")
print(entradas)

resultado = subprocess.run(
    ["python3", "dicionario3.py"],
    input=entradas,
    capture_output=True,
    text=True
)

print("Saida do programa:")
print(resultado.stdout)
