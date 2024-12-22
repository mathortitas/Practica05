# Ejercicio 6: Verificar números capicúa
print("Ejercicio 6: Verificar números capicúa")
def es_capicua(numero):
    str_num = str(numero)
    return str_num == str_num[::-1]

inicio = int(input("Ingrese el número inicial (3 cifras): "))
fin = int(input("Ingrese el número final (4 cifras): "))
while inicio <= fin:
    if es_capicua(inicio):
        print(f"{inicio} es capicúa")
    inicio += 1