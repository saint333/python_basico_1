#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
fecha=input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ")
dia=fecha[:fecha.find("/")]
mesaño=fecha[fecha.find("/")+1:]
mes=mesaño[:mesaño.find("/")]
año=mesaño[mesaño.find("/")+1:]
print(f"dia {dia}, mes {mes}, año {año}")