#Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.
def longuitud_palabras(frase):
    
    return {word:len(word) for word in frase.split()}
    

print(longuitud_palabras("david israel granados elias"))
print(longuitud_palabras("yebssabell liv abigail galan chapoñan"))