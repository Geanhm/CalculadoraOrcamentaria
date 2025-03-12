import math
from tkinter import messagebox


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
