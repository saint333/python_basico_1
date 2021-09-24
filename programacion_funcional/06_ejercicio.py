#Escribir una función reciba una lista de notas y devuelva la lista de calificaciones correspondientes a esas notas.
def cambio(nota):
    if nota < 5:
        return 'c'
    elif nota < 10:
        return 'b'
    elif nota < 15:
        return 'a'
    else:
        return 'ad'

def aplicando_cambio(notas):
    return list(map(cambio,notas))

print(aplicando_cambio([6.5, 5, 3.4, 8.2, 2.1, 9.7, 10,20]))