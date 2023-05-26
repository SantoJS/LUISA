import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

def calculate_deflection(L, E, I, w):
    x = np.linspace(0, L, 100)
    theta = (w * x**2) / (24 * E * I) * (L**2 - x**2)
    delta = (w * x**4) / (8 * E * I) * (1 - x**2 / L**2)
    max_theta = np.max(theta)
    max_delta = np.max(delta)
    return x, theta, delta, max_theta, max_delta

def plot_deflection(L, x, theta, delta, max_theta, max_delta):
    plt.figure()
    plt.subplot(211)
    plt.plot(x, theta)
    plt.xlabel('x')
    plt.ylabel('Theta')
    plt.title('Deflection Angle')

    # Mostrar el valor máximo de Theta en la gráfica
    plt.text(0.8 * L, max_theta, f'Max Theta = {max_theta:.4f}', fontsize=8, ha='left', va='bottom')

    plt.subplot(212)
    plt.plot(x, delta)
    plt.xlabel('x')
    plt.ylabel('Delta')
    plt.title('Deflection')

    # Mostrar el valor máximo de Delta en la gráfica
    plt.text(0.8 * L, max_delta, f'Max Delta = {max_delta:.4f}', fontsize=8, ha='left', va='bottom')

    plt.tight_layout()
    plt.show()

def calculate_button_click():
    L = float(length_entry.get())
    E = float(modulus_entry.get())
    I = float(moment_entry.get())
    w = float(load_entry.get())

    x, theta, delta, max_theta, max_delta = calculate_deflection(L, E, I, w)
    plot_deflection(L, x, theta, delta, max_theta, max_delta)

    result_text = f"Resultados:\n\nMax Theta = {max_theta:.4f}\nMax Delta = {max_delta:.4f}"
    result_label.config(text=result_text)

# Crear la ventana
window = tk.Tk()
window.title('Cálculo de Deflexión')

# Agregar un título al formulario
title_label = tk.Label(window, text='Cálculo de Deflexión de Viga', font=('Arial', 14, 'bold'))
title_label.pack()

# Crear los campos de entrada
length_label = tk.Label(window, text='Longitud (L):')
length_label.pack()
length_entry = tk.Entry(window)
length_entry.pack()

modulus_label = tk.Label(window, text='Módulo de elasticidad (E):')
modulus_label.pack()
modulus_entry = tk.Entry(window)
modulus_entry.pack()

moment_label = tk.Label(window, text='Momento de inercia (I):')
moment_label.pack()
moment_entry = tk.Entry(window)
moment_entry.pack()

load_label = tk.Label(window, text='Carga distribuida (w):')
load_label.pack()
load_entry = tk.Entry(window)
load_entry.pack()

calculate_button = tk.Button(window, text='Calcular', command=calculate_button_click)
calculate_button.pack()

# Resultado
result_label = tk.Label(window, text='Resultados:')
result_label.pack()

# Iniciar la ventana
window.mainloop()
