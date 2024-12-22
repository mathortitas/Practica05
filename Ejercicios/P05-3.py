# Ejercicio 3: Validar un nombre y apellido
print("Ejercicio 3: Validar un nombre y apellido")
def validar_nombre_apellido(nombre):
    return nombre.isalpha()

while True:
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    if validar_nombre_apellido(nombre) and validar_nombre_apellido(apellido):
        print(f"Nombre completo válido: {nombre} {apellido}")
        break
    else:
        print("Nombre o apellido no válidos. Intente nuevamente.")