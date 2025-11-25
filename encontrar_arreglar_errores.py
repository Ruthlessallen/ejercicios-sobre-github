# Lista de prueba
lista_ejemplo = ["manzana", "banana", "manzana", "pera", "banana", "manzana"]

def contar_palabras(lista):
    frecuencias = {}  # Error 1: Tipo de dato incorrecto
    for palabra in lista: # Error 2: Recorre la lista incorrecta
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1 # Error 3: Sintaxis incorrecta
    return frecuencias

# Llamada a la función (no tocar esta parte, debe funcionar con la corrección)
resultado = contar_palabras(lista_ejemplo)
print(resultado)