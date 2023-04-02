pizza = int(input("Escoge qué tipo de pizza quieres: 1. Vegetariana 2. Normal: "))

if pizza == 1:
    opcion_ingrediente = int(input("Escoge un ingrediente: 1. Pimiento 2. Tofu: "))
    if opcion_ingrediente == 1:
        print(f"Tu pizza es vegetariana y tiene mozzarella, tomate y pimiento.")
    elif opcion_ingrediente == 2:
        print("Tu pizza es vegetariana y tiene mozzarella, tomate y tofu.")
    else:
        print("Opción incorrecta.")

if pizza == 2:
    opcion_ingrediente =int(input("Escoge un ingrediente: 1. peperoni 2. jamón 3. salmón: "))
    if opcion_ingrediente == 1:
        print("Tu pizza es normal y tiene mozzarella, tomate y peperoni.")
    elif opcion_ingrediente == 2:
        print("Tu pizza es normal y tiene mozzarella, tomate y jamón.")
    elif opcion_ingrediente == 3:
        print("Tu pizza es normal y tiene mozzarella, tomate y salmón.")
    else:
        print("opción incorrecta.")