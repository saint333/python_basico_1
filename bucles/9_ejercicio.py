#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
contra="contraseña"
while True:
    verificacion=input("Ingrese su contraseña: ")
    if verificacion == contra:
        print("Gracias por entrar")
        break
    else:
        print("fallo,vuelva a intentarlo")