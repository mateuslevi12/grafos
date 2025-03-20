# TRABALHO GRAFOS
# EQUIPE: MATEUS LEVI, VICTOR RIOS, GABRIEL DE PAULA E CAINÃ RIOS
# SOLUÇÃO BALDE DE TINTA
# BFS E vizinhança 8-conectada

import numpy as np
from collections import deque

def ler_matriz_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r') as f:
        matriz = [list(map(int, linha.split())) for linha in f.readlines()]
    return np.array(matriz)

def criar_grafo(matriz):
    linhas, colunas = matriz.shape
    grafo = {}
    
    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1), 
                (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    for r in range(linhas):
        for c in range(colunas):
            grafo[(r, c)] = []
            for dr, dc in direcoes:
                nr, nc = r + dr, c + dc
                if 0 <= nr < linhas and 0 <= nc < colunas:
                    grafo[(r, c)].append((nr, nc))
    
    return grafo

def preenchimento_balde(matriz, linha, coluna, nova_cor):
    linhas, colunas = matriz.shape
    cor_original = matriz[linha, coluna]
    if cor_original == nova_cor:
        return matriz
    
    grafo = criar_grafo(matriz)
    fila = deque([(linha, coluna)])
    
    while fila:
        r, c = fila.popleft()
        if matriz[r, c] == cor_original:
            matriz[r, c] = nova_cor
            for nr, nc in grafo[(r, c)]:
                if matriz[nr, nc] == cor_original:
                    fila.append((nr, nc))
    
    return matriz

caminho_arquivo = "data/UNIFOR_sample.txt"

matriz_exemplo = ler_matriz_arquivo(caminho_arquivo)

linha_inicial, coluna_inicial = 7, 6
nova_cor = 2

matriz_modificada = preenchimento_balde(matriz_exemplo.copy(), linha_inicial, coluna_inicial, nova_cor)

print("Matriz Modificada:")
for linha in matriz_modificada:
    print(" ".join(map(str, linha)))