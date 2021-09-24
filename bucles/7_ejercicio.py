#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 12.
for i in range(1, 13):
    for j in range(1, 13):
        print(i*j, end="\t")
    print("")