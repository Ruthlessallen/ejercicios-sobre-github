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


a = 10
b = 5
suma =a+b 
print(suma)
resta = a-b
print(resta)

print(a*b)
# Llamada a la función (no tocar esta parte, debe funcionar con la corrección)
resultado = contar_palabras(lista_ejemplo)
print(resultado)