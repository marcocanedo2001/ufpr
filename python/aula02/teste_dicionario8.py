import subprocess

print("Entradas do teste:")
print("O programa usa dois dicionarios fixos dentro do arquivo.")

resultado = subprocess.run(
    ["python3", "dicionario8.py"],
    capture_output=True,
    text=True
)

print("Saida do programa:")
print(resultado.stdout)
