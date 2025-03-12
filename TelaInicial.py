import tkinter as tk

from Main import abrir_calculo

tela_inicial = tk.Tk()
tela_inicial.title("Escolha um Cálculo")

tk.Label(tela_inicial, text="Escolha um tipo de cálculo:",
         font=("Arial", 14)).pack()
tk.Button(tela_inicial, text="Peso da Peça",
          command=lambda: abrir_calculo("peso")).pack()
tk.Button(tela_inicial, text="Área do Quadrado",
          command=lambda: abrir_calculo("quadrado")).pack()
tk.Button(tela_inicial, text="Área do Retângulo",
          command=lambda: abrir_calculo("retangulo")).pack()
tk.Button(tela_inicial, text="Área do Cilindro",
          command=lambda: abrir_calculo("cilindro")).pack()

tela_inicial.mainloop()
