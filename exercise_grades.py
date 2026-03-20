def grades():
    """
    Ejercicio 11 - Promedio de Calificaciones

    Dadas tres notas, calcular e imprimir:
    1. El promedio de las tres notas
    2. La nota máxima
    3. La nota mínima
    4. Cuántos puntos faltan del promedio a 10
    """
    nota1 = 8
    nota2 = 7
    nota3 = 9

    promedio = (nota1 + nota2 + nota3) / 3
    nota_maxima = nota3
    nota_minima = nota2
    puntos_faltantes = 10 - promedio

    print("El promedio de las tres notas es", promedio)
    print("La nota maxima es", nota_maxima)
    print("La nota minima es", nota_minima)
    print("Al promedio le faltan",puntos_faltantes, "puntos para llegar a 10")

