#Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos tuplas y muestre por pantalla su producto escalar.
a = (1, 2, 3)
b = (-1, 0, 2)
producto = 0
for i in range(len(a)):
    producto += a[i]*b[i]
print("El producto de los vectores " + str(a) + " y " + str(b) + " es " + str(producto)) 
