#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
contraseña="holamundo123"
contra=input("Escriba tu contraseña: ")
if contra.lower()==contraseña.lower():
    print("contraseña valida")
else:
    print("contraseña invalida")