def es_primo(x):
    if x < 2:  # Los números menores a 2 no son primos
        return False
    for n in range(2, int(x ** 0.5) + 1):  # Iterar hasta la raíz cuadrada de x
        if x % n == 0:  # Si es divisible por algún número en el rango, no es primo
            return False
    return True