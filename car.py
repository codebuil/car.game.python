import tkinter as tk
import time
import random

# Configurações da janela
janela = tk.Tk()
janela.title("Jogo do Carro")
janela.geometry("800x400")
janela.configure(bg="lightblue")  # Mudou a cor de fundo para azul para representar um cenário diferente
janela.resizable(False, False)

# Configuração da grade 16x16
for i in range(16):
    janela.grid_columnconfigure(i, weight=1)

# Inicialização das coordenadas do carro
carro_x, carro_y = 0, 7

# Inicialização das bolas (agora representando obstáculos na estrada)
obstaculos = []

# Inicialização do score
score = 0

# Função para criar um novo obstáculo
def criar_obstaculo():
    novo_obstaculo = {
        'x': 15,
        'y': random.randint(0, 15)
    }
    obstaculos.append(novo_obstaculo)

# Função para mover os obstáculos
def mover_obstaculos():
    for obstaculo in obstaculos:
        obstaculo['x'] -= 1

# Função para verificar colisões com os obstáculos
def verificar_colisoes():
    global score

    for obstaculo in obstaculos:
        if obstaculo['x'] == carro_x and obstaculo['y'] == carro_y:
            score -= 5
            obstaculos.remove(obstaculo)

# Função para desenhar o jogo
def desenhar_jogo():
    # Limpar a tela
    tela.delete("all")

    # Desenhar o carro (substituiu o avião)
    tela.create_text(carro_x * 50 + 25, carro_y * 25 + 12.5, text="🚕", font=("Console", 20))

    # Desenhar os obstáculos (substituiu as bolas)
    for obstaculo in obstaculos:
        tela.create_text(obstaculo['x'] * 50 + 25, obstaculo['y'] * 25 + 12.5, text="🏎️", font=("Console", 20))

    # Atualizar o score na barra de título
    janela.title(f"Jogo do Carro - Score: {score}")

    # Verificar colisões
    verificar_colisoes()

    # Mover os obstáculos
    mover_obstaculos()

    # Criar um novo obstáculo aleatoriamente
    if random.random() < 0.1:
        criar_obstaculo()

    # Chamar a função novamente após um intervalo de tempo
    janela.after(100, desenhar_jogo)

# Criar uma tela para desenhar o jogo
tela = tk.Canvas(janela, width=800, height=400, bg="lightblue")
tela.pack()

# Registrar a função para eventos de teclado (movimento vertical do carro)
def mover_carro(event):
    global carro_y

    if event.keysym == "Up" and carro_y > 0:
        carro_y -= 1
    elif event.keysym == "Down" and carro_y < 15:
        carro_y += 1

janela.bind("<Up>", mover_carro)
janela.bind("<Down>", mover_carro)

# Inicializar o jogo
desenhar_jogo()

janela.mainloop()
