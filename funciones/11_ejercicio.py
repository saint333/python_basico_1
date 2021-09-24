#Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.
def contar_palabras(texto):
    texto = texto.split()
    palabras = {}
    for i in texto:
        if i in palabras:
            palabras[i] += 1
        else:
            palabras[i] = 1
    return palabras

def most_repeated(palabras):
    mayor_palabra = ''
    cantidad = 0
    for palabra, numero in palabras.items():
        if numero > cantidad:
            mayor_palabra = palabra
            cantidad = numero
    return mayor_palabra, cantidad

texto = 'Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera'
print(contar_palabras(texto))
print(most_repeated(contar_palabras(texto)))