#Escribir un programa que pida al usuario un numero entero positivo y muestre por pantalla la cuenta atras desde ese numero hasta cero separado por comas.
num=int(input("Ingrese un numero entero positivo: "))
for i in range(num,-1,-1):
    print(i,end=", ")