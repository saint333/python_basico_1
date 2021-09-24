#Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.
def iva(descuento,iva=21):
    return descuento + descuento*iva/100
print(iva(1000,10))
print(iva(1000))