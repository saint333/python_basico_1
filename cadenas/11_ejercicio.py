#Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
producto=input("Nombre del producto: ")
precio=float(input("Precio: "))
unidades=int(input("Número de unidades: "))
total=precio*unidades
print(f"{producto}: {unidades:3d} unidades x {precio:6.2f}$ = {total:8.2f}$")