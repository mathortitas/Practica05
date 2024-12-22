# Ejercicio 7: Validar un DNI
print("Ejercicio 7: Validar un DNI")
def validar_dni(dni):
    return dni.isdigit() and len(dni) == 8

while True:
    dni = input("Ingrese su DNI: ")
    if validar_dni(dni):
        print(f"DNI válido: {dni}")
        break
    else:
        print("DNI inválido. Intente nuevamente.")
