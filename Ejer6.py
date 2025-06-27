import random

# Solicitar dimensiones
n = int(input("Ingrese el número de filas (N): "))
m = int(input("Ingrese el número de columnas (M): "))

# Generar matriz aleatoria con números entre 1 y 100
matriz = []
for i in range(n):
    fila = [random.randint(1, 100) for _ in range(m)]
    matriz.append(fila)

# Mostrar la matriz
print("\nMatriz generada:")
for fila in matriz:
    print(fila)

# Solicitar número a buscar
numero = int(input("\nIngrese el número que desea contar: "))

# Contar cuántas veces aparece el número
contador = 0
for fila in matriz:
    contador += fila.count(numero)

print(f"\nEl número {numero} aparece {contador} veces en la matriz.")
