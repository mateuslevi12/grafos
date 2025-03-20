import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from collections import deque

def carregar_imagem(caminho_imagem):
    imagem = Image.open(caminho_imagem).convert('L')
    matriz_imagem = np.array(imagem)
    return matriz_imagem

def salvar_imagem(matriz_imagem, caminho_saida):
    imagem = Image.fromarray(matriz_imagem.astype(np.uint8))
    imagem.save(caminho_saida)

def exibir_imagens(original, modificada):
    fig, eixos = plt.subplots(1, 2, figsize=(12, 6))
    eixos[0].imshow(original, cmap='gray')
    eixos[0].set_title("Imagem Original")
    eixos[1].imshow(modificada, cmap='gray')
    eixos[1].set_title("Imagem Modificada")
    plt.show()

def preenchimento_balde(imagem, linha, coluna, nova_cor):
    linhas, colunas = imagem.shape
    cor_original = imagem[linha, coluna]
    if cor_original == nova_cor:
        return imagem
    
    fila = deque([(linha, coluna)])
    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1), 
                (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    while fila:
        r, c = fila.popleft()
        if imagem[r, c] == cor_original:
            imagem[r, c] = nova_cor
            for dr, dc in direcoes:
                nr, nc = r + dr, c + dc
                if 0 <= nr < linhas and 0 <= nc < colunas and imagem[nr, nc] == cor_original:
                    fila.append((nr, nc))
    
    return imagem

caminho_imagem = "imgs/UNIFOR_grayscale.png"
caminho_saida = "output/UNIFOR_grayscale_output.png"

matriz_imagem = carregar_imagem(caminho_imagem)

linha_inicial, coluna_inicial = 304, 406
nova_cor = 150

imagem_modificada = preenchimento_balde(matriz_imagem.copy(), linha_inicial, coluna_inicial, nova_cor)

salvar_imagem(imagem_modificada, caminho_saida)
exibir_imagens(matriz_imagem, imagem_modificada)
