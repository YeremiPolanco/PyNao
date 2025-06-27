# Ingresar dimensiones de la matriz
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

# Ingresar los valores de la matriz
matriz = []
print("\nIngrese los valores de la matriz:")
for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = int(input(f"Ingrese valor en posición [{i}][{j}]: "))
        fila.append(valor)
    matriz.append(fila)

# Mostrar la matriz
print("\nMatriz ingresada:")
for fila in matriz:
    print(fila)

# Calcular la suma de cada fila y encontrar la de mayor suma
mayor_suma = sum(matriz[0])
indice_max = 0

for i in range(1, filas):
    suma_fila = sum(matriz[i])
    if suma_fila > mayor_suma:
        mayor_suma = suma_fila
        indice_max = i

print(f"\nLa fila con la mayor suma es la fila {indice_max}, con una suma de {mayor_suma}.")
