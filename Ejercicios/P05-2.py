# Ejercicio 2: Imprimir la tabla completa de multiplicar de un número
print("Ejercicio 2: Imprimir la tabla completa de multiplicar de un número")
def imprimir_tabla(numero):
    i = 1
    while i <= 10:
        print(f"{numero} x {i} = {numero * i}")
        i += 1

numero = int(input("Ingrese un número para generar su tabla de multiplicar: "))
imprimir_tabla(numero)

print("\n")