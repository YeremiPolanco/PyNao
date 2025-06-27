def generar_cuadrado_magico(n):
    if n % 2 == 0:
        raise ValueError("Este generador solo funciona con tamaños impares.")

    cuadrado = [[0] * n for _ in range(n)]
    num = 1
    i, j = 0, n // 2

    while num <= n ** 2:
        cuadrado[i][j] = num
        num += 1
        nuevo_i = (i - 1) % n
        nuevo_j = (j + 1) % n
        if cuadrado[nuevo_i][nuevo_j]:
            i = (i + 1) % n
        else:
            i, j = nuevo_i, nuevo_j

    return cuadrado

# Entradas del usuario
n = int(input("¿Qué tamaño de cuadrado mágico deseas? (solo impar, como 3, 5, 7): "))
suma_deseada = int(input("¿Qué suma deseas por fila/columna/diagonal?: "))

try:
    # Generar cuadrado mágico base
    cuadrado = generar_cuadrado_magico(n)

    # Calcular suma mágica estándar
    suma_original = sum(cuadrado[0])

    # Calcular el factor de escala
    factor = suma_deseada / suma_original

    # Escalar el cuadrado con redondeo
    cuadrado_escalado = [[round(celda * factor) for celda in fila] for fila in cuadrado]

    # Mostrar resultados
    print(f"\nCuadrado mágico escalado ({n}x{n}) con suma deseada = {suma_deseada}:\n")
    for fila in cuadrado_escalado:
        print(fila)

    # Verificación
    verificacion = sum(cuadrado_escalado[0])
    print(f"\nVerificación: suma de la primera fila = {verificacion}")
    if verificacion != suma_deseada:
        print("⚠️ Advertencia: no se puede obtener exactamente la suma deseada con redondeo entero.")

except ValueError as ve:
    print(f"\nError: {ve}")
