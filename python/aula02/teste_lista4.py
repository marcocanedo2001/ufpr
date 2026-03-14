import subprocess

entradas = "casa\nbola\nlivro\nmesa\nsol\ncarro\n"

print("Entradas do teste:")
print(entradas)

resultado = subprocess.run(
    ["python3", "lista4.py"],
    input=entradas,
    capture_output=True,
    text=True
)

print("Saida do programa:")
print(resultado.stdout)
