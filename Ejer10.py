# Ingresar dimensiones
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

# Ingresar la matriz de palabras
matriz = []
print("\nIngrese las palabras para la matriz:")
for i in range(filas):
    fila = []
    for j in range(columnas):
        palabra = input(f"Ingrese palabra en posición [{i}][{j}]: ")
        fila.append(palabra)
    matriz.append(fila)

# Mostrar la matriz ingresada
print("\nMatriz ingresada:")
for fila in matriz:
    print(fila)

# Obtener la palabra más larga de cada fila
palabras_largas = []
for fila in matriz:
    palabra_max = max(fila, key=len)
    palabras_largas.append(palabra_max)

# Mostrar resultado
print("\nPalabra más larga de cada fila:")
print(palabras_largas)
