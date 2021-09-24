#Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.
cesta=input("Ingrese los productos de la cesta de la compra separado por comas: ")
#print(cesta.replace(",","\n"))
print("\n".join(cesta.split(",")))