#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
n1=float(input("Ingrese el dividiendo: "))
n2=float(input("Ingrese el divisor: "))
if n2 == 0:
    #raise ZeroDivisionError    ->esto es para levantar una exepcion
    print("Ocurrio un error al dividir por cero")
else:
    print(f"La division es: {n1/n2}")