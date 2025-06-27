def transponer_matriz(matriz):
    n = len(matriz)  # número de filas (o columnas, ya que es cuadrada)
    transpuesta = []

    for j in range(n):  # iteramos columnas
        nueva_fila = []
        for i in range(n):  # iteramos filas
            nueva_fila.append(matriz[i][j])
        transpuesta.append(nueva_fila)

    return transpuesta


# Matriz cuadrada 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz original:")
for fila in matriz:
    print(fila)

transpuesta = transponer_matriz(matriz)

print("\nMatriz transpuesta:")
for fila in transpuesta:
    print(fila)
