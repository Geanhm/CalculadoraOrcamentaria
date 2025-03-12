# main.py
import math
import tkinter as tk
from tkinter import messagebox


def voltar_para_tela_inicial(root):
    root.destroy()
    iniciar_tela_inicial()


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
    tk.Button(root, text="Voltar",
              command=lambda: voltar_para_tela_inicial(root)).pack()
    root.mainloop()


def iniciar_tela_inicial():
    global tela_inicial
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


iniciar_tela_inicial()

# calculos.py


def calcular_peso(entry_densidade, entry_volume, resultado):
    try:
        densidade = float(entry_densidade.get())
        volume = float(entry_volume.get())
        resultado.set(f"Peso: {densidade * volume:.2f} kg")
    except ValueError:
        messagebox.showerror("Erro", "Insira valores numéricos válidos.")


def area_quadrado(entry_quadrado, resultado):
    try:
        lado = float(entry_quadrado.get())
        resultado.set(f"Área do quadrado: {lado ** 2:.2f} m²")
    except ValueError:
        messagebox.showerror("Erro", "Insira valores numéricos válidos.")


def area_retangulo(entry_base, entry_altura, resultado):
    try:
        base = float(entry_base.get())
        altura = float(entry_altura.get())
        resultado.set(f"Área do retângulo: {base * altura:.2f} m²")
    except ValueError:
        messagebox.showerror("Erro", "Insira valores numéricos válidos.")


def area_cilindro(entry_raio, entry_cilindro_altura, resultado):
    try:
        raio = float(entry_raio.get())
        altura = float(entry_cilindro_altura.get())
        area = 2 * math.pi * raio * (raio + altura)
        resultado.set(f"Área do cilindro: {area:.2f} m²")
    except ValueError:
        messagebox.showerror("Erro", "Insira valores numéricos válidos.")
