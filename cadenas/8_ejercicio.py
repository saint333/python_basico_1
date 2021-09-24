#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
producto=input("Ingrese el precio de un producto en euros con dos decimales: ")
print(producto[:producto.find(".")],"euros y", producto[producto.find(".")+1:],"centimos")