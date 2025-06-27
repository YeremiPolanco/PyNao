# Solicitar tamaño de la matriz cuadrada
n = int(input("Ingrese el tamaño de la matriz cuadrada (n x n): "))

# Ingresar los valores por consola
matriz = []
print("\nIngrese los valores de la matriz:")
for i in range(n):
    fila = []
    for j in range(n):
        valor = int(input(f"Ingrese valor en posición [{i}][{j}]: "))
        fila.append(valor)
    matriz.append(fila)

# Mostrar la matriz
print("\nMatriz ingresada:")
for fila in matriz:
    print(fila)

# Calcular la suma de la diagonal principal (donde i == j)
suma_diagonal = 0
for i in range(n):
    suma_diagonal += matriz[i][i]

print(f"\nLa suma de la diagonal principal es: {suma_diagonal}")
