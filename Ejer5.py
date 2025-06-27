def maximos_por_columna(matriz):
    columnas = len(matriz[0])
    maximos = []

    for j in range(columnas):
        max_col = matriz[0][j]
        for i in range(1, len(matriz)):
            if matriz[i][j] > max_col:
                max_col = matriz[i][j]
        maximos.append(max_col)

    return maximos

# Ingresar datos por consola para una matriz 4x3
matriz = []

print("Ingresa los valores de la matriz 4x3:")
for i in range(4):
    fila = []
    for j in range(3):
        valor = int(input(f"Ingrese valor para posición [{i}][{j}]: "))
        fila.append(valor)
    matriz.append(fila)

# Mostrar la matriz
print("\nMatriz ingresada:")
for fila in matriz:
    print(fila)

# Obtener y mostrar máximos por columna
resultado = maximos_por_columna(matriz)
print("\nMáximo de cada columna:", resultado)
