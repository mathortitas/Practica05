# Ejercicio 4: Verificar comentarios de alumnos
print("Ejercicio 4: Verificar comentarios de alumnos")
def verificar_comentario(comentario):
    palabras_negativas = ["malo", "pesimo", "no"]
    palabras_positivas = ["bueno", "excelente", "bien"]
    for palabra in palabras_negativas:
        if palabra in comentario.lower():
            return "Comentario NEGATIVO"
    for palabra in palabras_positivas:
        if palabra in comentario.lower():
            return "Comentario POSITIVO"
    return "Comentario NEUTRO"

comentario = input("Ingrese un comentario: ")
resultado = verificar_comentario(comentario)
print(resultado)
