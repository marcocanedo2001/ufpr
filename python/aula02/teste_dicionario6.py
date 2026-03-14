import subprocess

entradas = (
    "Ana\n20\n"
    "Bruno\n18\n"
    "Carla\n20\n"
    "Daniel\n18\n"
    "Eva\n21\n"
    "fim\n"
)

print("Entradas do teste:")
print(entradas)

resultado = subprocess.run(
    ["python3", "dicionario6.py"],
    input=entradas,
    capture_output=True,
    text=True
)

print("Saida do programa:")
print(resultado.stdout)
