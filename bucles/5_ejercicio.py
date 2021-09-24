#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
capital=float(input("Cantidad a invertir: "))
interes=float(input("Cual es el interes anual: "))
años=int(input("Años: "))
for i in range(años):
    capital *= 1 + interes/100
    print(f"Capital tras {i+1} años {round(capital, 2)}")