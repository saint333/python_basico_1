#Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.
def cuadrados(lista):
    lista_cuadrados=[i**2 for i in lista]
    """ 
    lista_cuadrados=[]
    for i in lista:
        lista_cuadrados.append(i**2)
     """
    return lista_cuadrados

print(cuadrados([1,2,3,4,5]))