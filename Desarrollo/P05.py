#Imprimir tabla del 3
i = 1
while i <= 10:
    print(f"3 x {i} = {3 * i}")
    i += 1

#Repetir una frase las veces que desee
def repetir_frase(frase, veces):
    i = 0
    while i < veces:
        print(frase)
        i += 1

frase = input("Ingrese la frase a repetir: ")
veces = int(input("¿Cuántas veces desea repetirla? "))
repetir_frase(frase, veces)

#Programa para solicitar ingreso de contraseña con intentos limitados:
password = ''
intentos = 0
max_intentos = 5

while password != '12345' and intentos < max_intentos:
    password = input("Por favor ingrese su contraseña: ")
    intentos += 1
    if password == '12345':
        print("¡Acceso concedido!")
    elif intentos == max_intentos:
        print("Finalizó los intentos...!")
#Programa que utiliza break para validar un nombre
while True:
    nombre = input("Ingrese su nombre: ")
    if nombre.isalpha():
        print(f"Nombre válido: {nombre}")
        break
    else:
        print("El nombre contiene caracteres inválidos. Intente nuevamente.")
# Programa que usa continue para validar nombre y contraseña en listas
nombres_validos = ["Alice", "Bob", "Carlos"]
contraseñas_validas = ["1234", "abcd", "5678"]

while True:
    nombre = input("Ingrese su nombre: ")
    if nombre not in nombres_validos:
        print("Nombre no válido. Intente nuevamente.")
        continue

    contraseña = input("Ingrese su contraseña: ")
    if contraseña not in contraseñas_validas:
        print("Contraseña no válida. Intente nuevamente.")
        continue

    print(f"¡Bienvenido, {nombre}!")
    break