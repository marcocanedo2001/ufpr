from unittest.mock import patch
import io
import runpy
from contextlib import redirect_stdout

numeros_teste = [10, 21, 32, 43, 54, 65, 76, 87, 98, 11]

print("Numeros aleatorios fixos usados no teste:")
print(numeros_teste)

saida = io.StringIO()

with patch("random.randint", side_effect=numeros_teste):
    with redirect_stdout(saida):
        runpy.run_path("lista3.py", run_name="__main__")

print("Saida do programa:")
print(saida.getvalue())
