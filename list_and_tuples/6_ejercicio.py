#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
cursos = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
desaprobados = []
for curso in cursos:
    nota = input("¿Qué nota has sacado en " + curso + "?: ")
    if nota >"11":
        desaprobados.append(curso)
    
for curso in desaprobados:
    cursos.remove(curso)

print(f"asignatura repetir es: {cursos}")