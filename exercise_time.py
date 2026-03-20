def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """
    total_segundos = 3665

    Horas = total_segundos // 3600
    resto = total_segundos % 3600
    Minutos = resto // 60
    Segundos = resto % 60

    print("Horas completas: ", Horas)
    print("Minutos restantes: ", Minutos)
    print("Segundos restantes: ", Segundos)
time()
