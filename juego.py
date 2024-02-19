import matplotlib.pyplot as plt
import numpy as np
import random

def draw_grid(grid):
    fig, ax = plt.subplots()
    ax.imshow(grid, cmap='binary')
    ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
    ax.set_xticks(np.arange(-0.5, 6, 1))
    ax.set_yticks(np.arange(-0.5, 6, 1))
    plt.show()

def create_square():
    grid = np.zeros((6, 6))
    grid[1:3, 1:3] = 1
    draw_grid(grid)

def create_rectangle():
    grid = np.zeros((6, 6))
    grid[4:6, 1:4] = 1
    draw_grid(grid)

def create_triangle():
    grid = np.zeros((6, 6))
    grid[2, 4] = grid[1, 5] = grid[3, 5] = 1
    draw_grid(grid)

def create_large_triangle():
    grid = np.zeros((6, 6))
    grid[1, 2] = grid[2, 1] = grid[2, 3] = grid[3, 0] = grid[3, 4] = grid[4, 1] = grid[4, 3] = grid[5, 2] = 1
    draw_grid(grid)

# Lista de funciones
functions = [create_square, create_rectangle, create_triangle, create_large_triangle]

# Pedir al usuario que introduzca el número de rondas
num_rounds = int(input("Por favor, introduce el número de rondas: "))

# Asegurarse de que el número de rondas no sea mayor que el número de funciones
if num_rounds > len(functions):
    print("El número de rondas no puede ser mayor que el número de figuras disponibles.")
else:
    for _ in range(num_rounds):
        # Seleccionar una función aleatoria y eliminarla de la lista
        function = random.choice(functions)
        functions.remove(function)
        
        # Llamar a la función
        function()