"""
12. GRAFOS COM DICIONARIOS
    Representa um grafo direcionado sem usar funcoes.
"""

import heapq

grafo = {
    "A": [("B", 4), ("C", 2)],
    "B": [("C", 1), ("D", 5)],
    "C": [("D", 8), ("E", 10)],
    "D": [("E", 2)],
    "E": []
}

# Adicionar vertice
novo_vertice = "F"
if novo_vertice not in grafo:
    grafo[novo_vertice] = []

# Adicionar aresta
vertice_origem = "E"
vertice_destino = "F"
peso_aresta = 3
if vertice_origem not in grafo:
    grafo[vertice_origem] = []
if vertice_destino not in grafo:
    grafo[vertice_destino] = []
grafo[vertice_origem].append((vertice_destino, peso_aresta))

print("Grafo inicial:", grafo)

# BFS
vertice_inicial = "A"
visitados_bfs = []
fila_bfs = [vertice_inicial]

while len(fila_bfs) > 0:
    vertice_atual = fila_bfs.pop(0)

    if vertice_atual not in visitados_bfs:
        visitados_bfs.append(vertice_atual)

        for vizinho, peso in grafo.get(vertice_atual, []):
            if vizinho not in visitados_bfs and vizinho not in fila_bfs:
                fila_bfs.append(vizinho)

print("BFS a partir de A:", visitados_bfs)

# DFS
visitados_dfs = []
pilha_dfs = [vertice_inicial]

while len(pilha_dfs) > 0:
    vertice_atual = pilha_dfs.pop()

    if vertice_atual not in visitados_dfs:
        visitados_dfs.append(vertice_atual)

        adjacentes = grafo.get(vertice_atual, [])
        for vizinho, peso in reversed(adjacentes):
            if vizinho not in visitados_dfs:
                pilha_dfs.append(vizinho)

print("DFS a partir de A:", visitados_dfs)

# Dijkstra
vertice_origem = "A"
vertice_destino = "E"
distancias = {}
anteriores = {}
fila_prioridade = []

for nome_vertice in grafo:
    distancias[nome_vertice] = float("inf")
    anteriores[nome_vertice] = None

distancias[vertice_origem] = 0
heapq.heappush(fila_prioridade, (0, vertice_origem))

while len(fila_prioridade) > 0:
    distancia_atual, nome_vertice_atual = heapq.heappop(fila_prioridade)

    if distancia_atual > distancias[nome_vertice_atual]:
        continue

    for vizinho, peso in grafo[nome_vertice_atual]:
        nova_distancia = distancia_atual + peso

        if nova_distancia < distancias[vizinho]:
            distancias[vizinho] = nova_distancia
            anteriores[vizinho] = nome_vertice_atual
            heapq.heappush(fila_prioridade, (nova_distancia, vizinho))

caminho = []
vertice_atual = vertice_destino

if distancias[vertice_destino] != float("inf"):
    while vertice_atual is not None:
        caminho.append(vertice_atual)
        vertice_atual = anteriores[vertice_atual]

    caminho.reverse()

print("Menor caminho de A ate E:", caminho)
print("Distancia total:", distancias[vertice_destino])

# Detectar ciclo antes
visitados = set()
tem_ciclo = False
pilha_controle = []

for nome_vertice_inicial in grafo:
    if nome_vertice_inicial in visitados:
        continue

    pilha_controle.append((nome_vertice_inicial, "entrando"))

    while len(pilha_controle) > 0:
        nome_vertice_atual, estado = pilha_controle.pop()

        if estado == "saindo":
            continue

        if nome_vertice_atual not in visitados:
            visitados.add(nome_vertice_atual)
            pilha_controle.append((nome_vertice_atual, "saindo"))

            for vizinho, peso in reversed(grafo.get(nome_vertice_atual, [])):
                if vizinho not in visitados:
                    pilha_controle.append((vizinho, "entrando"))
                else:
                    vizinho_ativo = False
                    for item in pilha_controle:
                        if item[0] == vizinho and item[1] == "saindo":
                            vizinho_ativo = True
                    if vizinho_ativo:
                        tem_ciclo = True

print("O grafo tem ciclo?", tem_ciclo)

# Adicionar aresta que cria ciclo
grafo["F"].append(("B", 1))

visitados = set()
tem_ciclo = False
pilha_controle = []

for nome_vertice_inicial in grafo:
    if nome_vertice_inicial in visitados:
        continue

    pilha_controle.append((nome_vertice_inicial, "entrando"))

    while len(pilha_controle) > 0:
        nome_vertice_atual, estado = pilha_controle.pop()

        if estado == "saindo":
            continue

        if nome_vertice_atual not in visitados:
            visitados.add(nome_vertice_atual)
            pilha_controle.append((nome_vertice_atual, "saindo"))

            for vizinho, peso in reversed(grafo.get(nome_vertice_atual, [])):
                if vizinho not in visitados:
                    pilha_controle.append((vizinho, "entrando"))
                else:
                    vizinho_ativo = False
                    for item in pilha_controle:
                        if item[0] == vizinho and item[1] == "saindo":
                            vizinho_ativo = True
                    if vizinho_ativo:
                        tem_ciclo = True

print("O grafo tem ciclo depois da nova aresta?", tem_ciclo)

# Remover vertice
vertice_para_remover = "F"
if vertice_para_remover in grafo:
    del grafo[vertice_para_remover]

for nome_vertice in grafo:
    nova_lista = []
    for vizinho, peso in grafo[nome_vertice]:
        if vizinho != vertice_para_remover:
            nova_lista.append((vizinho, peso))
    grafo[nome_vertice] = nova_lista

print("Grafo apos remover F:", grafo)
