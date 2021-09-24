#Escribir una función que reciba otra función booleana y una lista, y devuelva otra lista con los elementos de la lista que devuelvan True al aplicarles la función booleana.
def numeros_par(funcion,lista):
    final = []
    for i in lista:
        if funcion(i):
            final.append(i)
    return final

def prueba(n):
    return n % 2 == 0

print(numeros_par(prueba,[1,2,3,4,5,6]))