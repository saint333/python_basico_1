#Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.
cursos={'Matemáticas': 6, 'Física': 4, 'Química': 5}
total_credito=0
for materia,credito in cursos.items():
    print(f"{materia} tiene {credito}")
    total_credito += credito
print("El total de credito es:",total_credito)