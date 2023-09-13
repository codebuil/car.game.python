import tkinter as tk
import winsound

# Configurações da janela
janela = tk.Tk()
janela.title("Jogo do Sorriso")
janela.geometry("400x400")
janela.configure(bg="lightyellow")

# Configuração da grade 16x16
for i in range(16):
    janela.grid_columnconfigure(i, weight=1)
    janela.grid_rowconfigure(i, weight=1)

# Inicialização das coordenadas do sorriso
x, y = 0, 0

# Função para mover o sorriso
def mover_sorriso(event):
    global x, y

    if event.keysym == "Up" and y > 0:
        y -= 1
    elif event.keysym == "Down" and y < 15:
        y += 1
    elif event.keysym == "Left" and x > 0:
        x -= 1
    elif event.keysym == "Right" and x < 15:
        x += 1
    else:
        winsound.Beep(500, 100)  # Emitir som de "beep" quando o usuário tenta sair

    desenhar_sorriso()

# Função para desenhar o sorriso
def desenhar_sorriso():
    for i in range(16):
        for j in range(16):
            lbl = tk.Label(janela, text=" ", font=("Courier", 12), bg="lightyellow", fg="yellow")
            lbl.grid(row=i, column=j, sticky="nsew")

    lbl_sorriso = tk.Label(janela, text="😃", font=("Courier", 12) , bg="lightyellow", fg="yellow")
    lbl_sorriso.grid(row=y, column=x, sticky="nsew")

# Registrar a função para eventos de teclado
janela.bind("<Up>", mover_sorriso)
janela.bind("<Down>", mover_sorriso)
janela.bind("<Left>", mover_sorriso)
janela.bind("<Right>", mover_sorriso)

# Inicializar o sorriso na posição (0, 0)
desenhar_sorriso()

janela.mainloop()
