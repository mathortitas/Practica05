# Programa que busca el número 2 en una lista de números
print("Programa que busca el número 2 en una lista de números")
valores = [5, 1, 9, 2, 7, 4]
encontrado = False
indice = 0
longitud = len(valores)

while not encontrado and indice < longitud:
    if valores[indice] == 2:
        encontrado = True
    else:
        indice += 1

if encontrado:
    print(f'El número 2 ha sido encontrado en el índice {indice}')
else:
    print('El número 2 no se encuentra en la lista')

print("\n")

# Programa que solicita ingreso de contraseña con intentos limitados
print("Programa que solicita ingreso de contraseña con intentos limitados")
password = ''
cont = 0
max_intentos = 5

while password != '12345' and cont < max_intentos:
    password = input("Por favor ingrese su contraseña: ")
    cont += 1
    if password == '12345':
        print("¡Acceso concedido!")
    elif cont == max_intentos:
        print("Finalizo los intentos...!")

if cont < max_intentos:
    print("Por fin...!")

print("\n")

# Programa que imprime la secuencia 3n+1 desde un número dado
print("Programa que imprime la secuencia 3n+1 desde un número dado")
def seq3np1(n):
    while n != 1:
        print(n, end=", ")
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    print(n, end=".\n")

num = int(input('Ingrese numero de inicio n : ==> '))
seq3np1(num)

print("\n")

# Programa que cuenta los dígitos "0" y "5" en un entero positivo
print("Programa que cuenta los dígitos \"0\" y \"5\" en un entero positivo")
def contar_ceros_y_cincos(numero):
    contador = 0
    while numero > 0:
        digito = numero % 10
        if digito == 0 or digito == 5:
            contador += 1
        numero = numero // 10
    return contador

numero = int(input('Ingrese un numero que contenga los digitos "0" y "5" : ==> '))
cantidad = contar_ceros_y_cincos(numero)
print(f'La cantidad de dígitos "0" y "5" en el numero {numero} es: {cantidad}')