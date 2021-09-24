#Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.
def cuadrados(lista):
    lista_cuadrados=[i**2 for i in lista]
    return lista_cuadrados

def estadistica(lista):
    dato={}
    dato["media"]=sum(lista)/len(lista)
    dato["varianza"]=sum(cuadrados(lista))/len(lista)-dato["media"]**2
    dato["desviacion tipica"]=round(dato["varianza"]**0.5,2)
    return dato

print(estadistica([1,2,3,4,5]))