#Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.
def circulo(radio):
    return 3.14*radio**2

def cilindro(radio,altura):
    return circulo(radio)*altura

print(circulo(2))
print(cilindro(2,3))