#Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.
facturas={}
pagado=0
pendiente= 0
salir= ""
while salir != "S":
    if salir == "A":
        clave=input("Número de factura: ")
        valor=float(input("Cantidad de pago: "))
        facturas[clave]=valor
        pendiente += valor
    elif salir == "P":
        clave=input("Introduce el número de factura a pagar: ")
        valor=facturas.pop(clave,0)
        pagado+=valor
        pendiente-= valor
    print('Recaudado:', pagado)
    print('Pendiente de cobro: ', pendiente)
    salir = input('¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (S)? ').upper()
    
