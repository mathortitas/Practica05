# Ejercicio 5: Generar listas aleatorias y clasificarlas
import random
print("Ejercicio 5: Generar listas aleatorias y clasificarlas")
def clasificar_multiplos(lista):
    multiplos_2 = []
    multiplos_3 = []
    multiplos_5 = []
    for num in lista:
        if num % 2 == 0:
            multiplos_2.append(num)
        if num % 3 == 0:
            multiplos_3.append(num)
        if num % 5 == 0:
            multiplos_5.append(num)
    return multiplos_2, multiplos_3, multiplos_5

numeros = [random.randint(1, 100) for _ in range(60)]
multiplos_2, multiplos_3, multiplos_5 = clasificar_multiplos(numeros)
print(f"Múltiplos de 2: {multiplos_2}")
print(f"Múltiplos de 3: {multiplos_3}")
print(f"Múltiplos de 5: {multiplos_5}")