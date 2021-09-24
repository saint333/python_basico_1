#Escribir una función que reciba un número entero positivo y devuelva su factorial.
def factorial(n):
    total= 1
    for i in range(n):
        total *= i+1
    return total

print(factorial(125))