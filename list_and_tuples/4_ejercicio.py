#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
loteria= []
for i in range(6):
    numero=int(input("ingrese un numero: "))
    loteria.append(numero)
loteria.sort()
print(f"los numeros ganodores son {loteria}")