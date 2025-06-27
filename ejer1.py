# Crear una matriz vacía
matriz = []

# Llenar la matriz con valores ingresados por el usuario
print("Ingresa los valores para una matriz de 4x4:")

for i in range(4):
    fila = []
    for j in range(4):
        valor = int(input(f"Ingrese el valor para posición [{i}][{j}]: "))
        fila.append(valor)
    matriz.append(fila)

# Mostrar la matriz
print("\nMatriz ingresada:")
for fila in matriz:
    print(fila)

# Contar números pares en toda la matriz
contador_pares = 0

for fila in matriz:
    for num in fila:
        if num % 2 == 0:
            contador_pares += 1

print(f"\nCantidad total de números pares: {contador_pares}")

# Contar impares por cada fila
print("\nCantidad de números impares por fila:")
for i in range(4):
    contador_impares = 0
    for num in matriz[i]:
        if num % 2 != 0:
            contador_impares += 1
    print(f"Fila {i}: {contador_impares} impares")
