import subprocess

entradas = (
    "Ana\n1111-1111\n"
    "Bruno\n2222-2222\n"
    "Carla\n3333-3333\n"
    "Daniel\n4444-4444\n"
    "Eva\n5555-5555\n"
    "Carla\n"
    "Paulo\n"
)

print("Entradas do teste:")
print(entradas)

resultado = subprocess.run(
    ["python3", "dicionario1.py"],
    input=entradas,
    capture_output=True,
    text=True
)

print("Saida do programa:")
print(resultado.stdout)
