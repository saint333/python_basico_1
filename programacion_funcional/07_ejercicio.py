#Escribir una función reciba un diccionario con la las asignaturas y las notas de un alumno y devuelva otro diccionario con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas.
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
    return {asignatura.upper():cambio(nota) for asignatura,nota in notas.items()}

print(aplicando_cambio({'Matemáticas':15.5, 'Física':15, 'Química':12, 'Economía':8.2, 'Historia':9.7, 'Programación':10}))