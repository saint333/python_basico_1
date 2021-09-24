#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
palabra = input("Ingrese cualquier palabra: ")
for i in range(10):#solucion 1
    print(palabra)
print("")
contador = 1 #solucion 2
while contador <= 10:
    print(palabra)
    contador+=1