def saludar(mensaje):
    print("Hola.")
    print("¿Cómo estás?")
    print(mensaje)
    print("Adiós.")

opcion = int(input("Escoge una opción (1,2,3) "))   

if opcion == 1:
    saludar("Elegiste la opción 1.")
elif opcion == 2:
    saludar("Elegiste la opción 2.")
elif opcion == 3:
    saludar("Elegiste la opción 3.")
else:
    print("Game Over.")