# Función para verificar si una palabra empieza con vocal
def empieza_con_vocal(palabra):
    return palabra[0].lower() in "aeiou"

# Ingresar tamaño de la matriz
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

# Ingresar palabras en la matriz
matriz = []
print("\nIngrese las palabras para la matriz:")
for i in range(filas):
    fila = []
    for j in range(columnas):
        palabra = input(f"Ingrese palabra en posición [{i}][{j}]: ")
        fila.append(palabra)
    matriz.append(fila)

# Mostrar la matriz
print("\nMatriz de palabras:")
for fila in matriz:
    print(fila)

# Contar palabras que comienzan con vocal
contador = 0
for fila in matriz:
    for palabra in fila:
        if palabra and empieza_con_vocal(palabra):
            contador += 1

print(f"\nCantidad total de palabras que comienzan con vocal: {contador}")
