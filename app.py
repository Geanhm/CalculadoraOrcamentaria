import math
import tkinter as tk
from tkinter import messagebox


def calcular_peso():
    try:
        densidade = float(entry_densidade.get())
        volume = float(entry_volume.get())
        resultado.set(f"Peso: {densidade * volume:.2f} kg")
    except ValueError:
        messagebox.showerror("Erro", "Insira valores numéricos válidos.")


def area_quadrado():
    try:
        lado = float(entry_quadrado.get())
        resultado.set(f"Área do quadrado: {lado ** 2:.2f} m²")
    except ValueError:
        messagebox.showerror("Erro", "Insira valores numéricos válidos.")


def area_retangulo():
    try:
        base = float(entry_base.get())
        altura = float(entry_altura.get())
        resultado.set(f"Área do retângulo: {base * altura:.2f} m²")
    except ValueError:
        messagebox.showerror("Erro", "Insira valores numéricos válidos.")


def area_cilindro():
    try:
        raio = float(entry_raio.get())
        altura = float(entry_cilindro_altura.get())
        area = 2 * math.pi * raio * (raio + altura)
        resultado.set(f"Área do cilindro: {area:.2f} m²")
    except ValueError:
        messagebox.showerror("Erro", "Insira valores numéricos válidos.")


root = tk.Tk()
root.title("Calculadora Geométrica")
resultado = tk.StringVar()

# Seção Peso da Peça
tk.Label(root, text="Densidade (kg/m³):").pack()
entry_densidade = tk.Entry(root)
entry_densidade.pack()
tk.Label(root, text="Volume (m³):").pack()
entry_volume = tk.Entry(root)
entry_volume.pack()
tk.Button(root, text="Calcular Peso", command=calcular_peso).pack()

# Seção Área Quadrado
tk.Label(root, text="Lado do Quadrado (m):").pack()
entry_quadrado = tk.Entry(root)
entry_quadrado.pack()
tk.Button(root, text="Calcular Área do Quadrado", command=area_quadrado).pack()

# Seção Área Retângulo
tk.Label(root, text="Base do Retângulo (m):").pack()
entry_base = tk.Entry(root)
entry_base.pack()
tk.Label(root, text="Altura do Retângulo (m):").pack()
entry_altura = tk.Entry(root)
entry_altura.pack()
tk.Button(root, text="Calcular Área do Retângulo",
          command=area_retangulo).pack()

# Seção Área Cilindro
tk.Label(root, text="Raio do Cilindro (m):").pack()
entry_raio = tk.Entry(root)
entry_raio.pack()
tk.Label(root, text="Altura do Cilindro (m):").pack()
entry_cilindro_altura = tk.Entry(root)
entry_cilindro_altura.pack()
tk.Button(root, text="Calcular Área do Cilindro", command=area_cilindro).pack()

# Exibir Resultado
tk.Label(root, textvariable=resultado, font=("Arial", 12, "bold")).pack()

root.mainloop()
