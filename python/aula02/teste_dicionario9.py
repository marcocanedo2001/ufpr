import subprocess

entradas = (
    "3\n"
    "Ana\n10\n"
    "Bruno\n20\n"
    "Carla\n30\n"
    "10\n20\n20\n30\n0\n99\n10\n-1\n"
)

print("Entradas do teste:")
print(entradas)

resultado = subprocess.run(
    ["python3", "dicionario9.py"],
    input=entradas,
    capture_output=True,
    text=True
)

print("Saida do programa:")
print(resultado.stdout)
