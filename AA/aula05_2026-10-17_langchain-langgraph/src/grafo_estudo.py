from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class Estado(TypedDict, total=False):
    texto: str
    simulada: str
    bruta: str
    sentimento: str
    erro: str

def verificar(s: Estado):
    texto = s.get("texto", "")
    valido = isinstance(texto, str) and bool(texto.strip())
    return {"erro": "" if valido else "entrada inválida"}

def rota(s: Estado):
    return "encerrar" if s["erro"] else "continuar"

def receber(s: Estado):
    return {"bruta": s.get("simulada", "")}

def validar(s: Estado):
    rotulo = s["bruta"].strip().lower()
    if rotulo not in {"positivo", "negativo"}:
        return {"sentimento": "", "erro": "saída inválida"}
    return {"sentimento": rotulo, "erro": ""}


g = StateGraph(Estado)
g.add_node("verificar", verificar)
g.add_node("receber", receber)
g.add_node("validar", validar)
g.add_edge(START, "verificar")
g.add_conditional_edges("verificar", rota, {
    "encerrar": END, "continuar": "receber"
})
g.add_edge("receber", "validar")
g.add_edge("validar", END)
app = g.compile()

ok = app.invoke({"texto": "Muito bom", "simulada": "Positivo"})
assert ok["sentimento"] == "positivo" and not ok["erro"]
vazio = app.invoke({"texto": " ", "simulada": "negativo"})
assert vazio["erro"] == "entrada inválida"
assert "bruta" not in vazio
ruim = app.invoke({"texto": "Bom", "simulada": "talvez"})
assert ruim["erro"] == "saída inválida"
print("Três caminhos verificados")
