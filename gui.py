import tkinter as tk
from tkinter import font
import random

# Função para criar um emoji de "sorte" aleatório
def emoji_sorte_aleatorio():
    emojis_sorte = ["😀", "😄", "😁", "😆", "😅", "😂", "🤣", "😊", "😇", "😍", "😎", "🥰", "😻", "🤩", "🥳", "🤞"]
    return random.choice(emojis_sorte)

# Configurações da janela
janela = tk.Tk()
janela.title("Grid de Emojis de Sorte")
janela.geometry("400x400")
janela.configure(bg="black")

# Configuração da grade 16x16
for i in range(16):
    janela.grid_columnconfigure(i, weight=1)
    janela.grid_rowconfigure(i, weight=1)

# Criação de rótulos com emojis de "sorte" e cor branca
for _ in range(50):
    row, col = random.randint(0, 15), random.randint(0, 15)
    emoji = emoji_sorte_aleatorio()
    lbl = tk.Label(janela, text=emoji, font=("Segoe UI", 12), bg="black", fg="white")
    lbl.grid(row=row, column=col, sticky="nsew")

janela.mainloop()
