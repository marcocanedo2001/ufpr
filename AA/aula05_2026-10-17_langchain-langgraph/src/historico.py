"""Prática autoral de histórico: preservar system e pares completos."""
import csv

def janela(mensagens, turnos=2):
    if not isinstance(turnos, int) or isinstance(turnos, bool) or turnos < 1:
        raise ValueError("Quantidade de turnos deve ser inteira e positiva")
    if not mensagens or mensagens[0][0] != "system":
        raise ValueError("Primeira mensagem precisa ser system")
    resto = mensagens[1:]
    if len(resto) % 2:
        raise ValueError("Esperados turnos completos")
    for i in range(0, len(resto), 2):
        if resto[i][0] != "human" or resto[i+1][0] not in {"assistant", "ai"}:
            raise ValueError("Ordem esperada: human e assistant")
    return [mensagens[0], *resto[-2*turnos:]]

def salvar_csv(caminho, mensagens, remover_virgulas=False):
    # remover_virgulas=True reproduz a simplificação pedida no slide.
    with open(caminho, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["papel", "conteudo"])
        for papel, texto in mensagens:
            w.writerow([papel, texto.replace(",", "") if remover_virgulas else texto])

def carregar_csv(caminho):
    with open(caminho, encoding="utf-8", newline="") as f:
        leitor = csv.DictReader(f)
        if leitor.fieldnames != ["papel", "conteudo"]:
            raise ValueError("Cabeçalho CSV inválido")
        return [(r["papel"], r["conteudo"]) for r in leitor]
