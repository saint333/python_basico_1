#Escribir una función que simule una calculadora científica que permita calcular el seno, coseno, tangente, exponencial y logaritmo neperiano. La función preguntará al usuario el valor y la función a aplicar, y mostrará por pantalla una tabla con los enteros de 1 al valor introducido y el resultado de aplicar la función a esos enteros.

from math import sin, cos, tan, exp, log

def calculadora():
    functiones = {'sin':sin, 'cos':cos, 'tan':tan, 'exp':exp, 'log':log}
    f = input('Introduce la función a aplicar (sin, cos, tan, exp, log): ')
    n = int(input('Introduce un entero positivo: '))
    resultados = [functiones[f](x) for x in range(1, n+1)]
    for i in range(n):
        print (i + 1, '\t', resultados[i])
    return

calculadora()