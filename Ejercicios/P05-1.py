# Ejercicio 1: Generar un rango y verificar si los números son pares o impares
print("Ejercicio 1: Generar un rango y verificar si los números son pares o impares")
def verificar_paridad(inicio, fin):
    while inicio <= fin:
        if inicio % 2 == 0:
            print(f"{inicio} es par")
        else:
            print(f"{inicio} es impar")
        inicio += 1

inicio = int(input("Ingrese el número inicial: "))
fin = int(input("Ingrese el número final: "))
verificar_paridad(inicio, fin)

print("\n")