"""Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

Lista de la compra	
Artículo 1	Precio
Artículo 2	Precio
Artículo 3	Precio
…	…
Total	Coste """
cesta={}
continuar=True
while continuar:
    artículo=input("Que articulo desea agregar: ")
    precio=float(input(f"El precio del {artículo} es : "))
    cesta[artículo] = precio
    continuar=input("Desea agregar otra cosa (si o no): ")
    if continuar=="si":
        continuar=True
    else:
        continuar=False

contador = 1
precio_total = 0
print("lista de productos")
for i,j in cesta.items():
    print(f"{contador}\t{i}\t{j}" )
    contador += 1
    precio_total += j
print(f"total\t\t{precio_total}")