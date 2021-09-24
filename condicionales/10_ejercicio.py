""" La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva. """
def ingredientes(eleccion):
    if eleccion == "1":
        ingredientes= input("""Eliga el ingredientes
        1.- Pimiento
        2.- Tofu
        >>>>>> """)
        if ingredientes == "1":
            ingrediente = "pimiento"
        else:
            ingrediente = "tofu"
    else:
        ingredientes= input("""Eliga el ingredientes
        1.- Peperoni
        2.- Jamon
        3.- Salmón
        >>>>>> """)
        if ingredientes == "1":
            ingrediente = "peperoni"
        elif ingredientes == "2":
            ingrediente = "jamon"
        else:
            ingrediente = "salmon"

    return ingrediente

def main():
    pizza=input("""La pizzería Bella Napoli
    1.- Vegetariana
    2.- No vegetariana
    ¿Cual desea?: """)

    if pizza == "1":
        tipo = "vegetariana"
    elif pizza == "2":
        tipo = "no vegetariana"
    else:
        print("Numero incorrecto")
        main()

    ingrediente = ingredientes(pizza)

    print(f"Tu tipo de pizza es {tipo} y tiene los siguientes ingredientes: mozzarrella, tomate y {ingrediente}")

if __name__=='__main__':
    main()