import subprocess

print("Entradas do teste:")
print("O programa usa usuarios, itens e avaliacoes fixas dentro do arquivo.")

resultado = subprocess.run(
    ["python3", "dicionario13.py"],
    capture_output=True,
    text=True
)

print("Saida do programa:")
print(resultado.stdout)
