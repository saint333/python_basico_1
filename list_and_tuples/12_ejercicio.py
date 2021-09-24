#Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una tupla y muestre por pantalla su media y desviación típica.
ejemplo = input("Introduce una muestra de números separados por comas: ")
ejemplo = ejemplo.split(',')
n = len(ejemplo)
for i in range(n):
    ejemplo[i] = int(ejemplo[i])
ejemplo = tuple(ejemplo)
suma = 0
sumacuadrados = 0
for i in ejemplo:
    suma += i
    sumacuadrados += i**2
media = suma/n
desviacion = (sumacuadrados/n-media**2)**(1/2)
print('La media es', media, ', y la desviación típica es', desviacion)