#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
while True:
    frase=input("Escriba una palabra: ")
    if frase == "salir":
        break
    print(frase)