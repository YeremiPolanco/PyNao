# Matriz 3x4 de ejemplo (puedes modificar los valores o pedirlos al usuario)
matriz = [
    [2, 4, 6, 8],
    [1, 3, 5, 7],
    [9, 0, 2, 4]
]

# Crear una lista con la suma de cada fila
suma_filas = []

for fila in matriz:
    suma = sum(fila)
    suma_filas.append(suma)

# Mostrar resultados
print("Matriz:")
for f in matriz:
    print(f)

print("\nSuma de cada fila:", suma_filas)
