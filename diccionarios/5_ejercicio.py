#Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
informacion={}
while True:
    clave=input("Que dato quieres introducir: ")
    valor=input(clave + ": ")
    informacion[clave] = valor
    print(informacion)
    nuevo = "si"
    nuevos=input("Quiere ingresar otro dato (si o no): ")
    if nuevo == nuevos:
        continue
    else:
        break
