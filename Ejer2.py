import random

# Función para buscar un número en la matriz
def buscar_numero(matriz, numero):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                return (i, j)  # Retorna la primera posición encontrada
    return 0  # No se encontró

# Solicitar tamaño de la matriz al usuario
filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))

# Generar matriz con valores aleatorios entre 15 y 45
matriz = []
for _ in range(filas):
    fila = [random.randint(15, 45) for _ in range(columnas)]
    matriz.append(fila)

# Mostrar la matriz generada
print("\nMatriz generada:")
for fila in matriz:
    print(fila)

# Solicitar número a buscar
numero_buscado = int(input("\nIngrese el número a buscar: "))

# Llamar a la función
resultado = buscar_numero(matriz, numero_buscado)

# Mostrar resultado
if resultado != 0:
    print(f"\nEl número {numero_buscado} se encontró en la posición: fila {resultado[0]}, columna {resultado[1]}")
else:
    print(f"\nEl número {numero_buscado} no se encuentra en la matriz.")
