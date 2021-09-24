#Escribir una función que reciba otra función y una lista, y devuelva otra lista con el resultado de aplicar la función dada a cada uno de los elementos de la lista.
def principal(funcion,lista):
    lista_final=[]
    for i in lista:
        lista_final.append(funcion(i))
    return lista_final

def cuadrados(n):
    return n**2

print(principal(cuadrados, [1,2,3,4,5]))