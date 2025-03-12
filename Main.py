import tkinter as tk
from Calculos import calcular_peso, area_quadrado, area_retangulo, area_cilindro
from tkinter import messagebox


def abrir_calculo(tipo):
    tela_inicial.destroy()
    global root, resultado
    root = tk.Tk()
    root.title("Calculadora Geométrica")
    resultado = tk.StringVar()

    if tipo == "peso":
        tk.Label(root, text="Densidade (kg/m³):").pack()
        entry_densidade = tk.Entry(root)
        entry_densidade.pack()
        tk.Label(root, text="Volume (m³):").pack()
        entry_volume = tk.Entry(root)
        entry_volume.pack()
        tk.Button(root, text="Calcular Peso", command=lambda: calcular_peso(
            entry_densidade, entry_volume, resultado)).pack()
        tk.Button(root, text='Voltar',
                  command=lambda: tela_inicial.mainloop().pack())

    elif tipo == "quadrado":
        tk.Label(root, text="Lado do Quadrado (m):").pack()
        entry_quadrado = tk.Entry(root)
        entry_quadrado.pack()
        tk.Button(root, text="Calcular Área do Quadrado",
                  command=lambda: area_quadrado(entry_quadrado, resultado)).pack()
    elif tipo == "retangulo":
        tk.Label(root, text="Base do Retângulo (m):").pack()
        entry_base = tk.Entry(root)
        entry_base.pack()
        tk.Label(root, text="Altura do Retângulo (m):").pack()
        entry_altura = tk.Entry(root)
        entry_altura.pack()
        tk.Button(root, text="Calcular Área do Retângulo", command=lambda: area_retangulo(
            entry_base, entry_altura, resultado)).pack()
    elif tipo == "cilindro":
        tk.Label(root, text="Raio do Cilindro (m):").pack()
        entry_raio = tk.Entry(root)
        entry_raio.pack()
        tk.Label(root, text="Altura do Cilindro (m):").pack()
        entry_cilindro_altura = tk.Entry(root)
        entry_cilindro_altura.pack()
        tk.Button(root, text="Calcular Área do Cilindro", command=lambda: area_cilindro(
            entry_raio, entry_cilindro_altura, resultado)).pack()

    tk.Label(root, textvariable=resultado, font=("Arial", 12, "bold")).pack()
    root.mainloop()


# Tela inicial
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
