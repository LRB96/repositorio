#Crear la función incializadora 
#Crear función principal (run) 
#Crear variable para almacenar número que le pido al usuario con input, y convertirlo en entero con int.
#Crear condicional if y else para saber si el número es primo o no. 
#En el if se escribe que el número  al cuadrado, y módulo 2 sea igual 0.
#Si el módulo 2 es 0 el número es par, y por ende no es primo.
#Si el módulo 2 no es 0, el número es impar, y por ende es primo.

def run():
    numero = int(input("Escribe un número: "))

    if (numero**2)%2 == 0:
        print("No es primo.")
    else:
        print("Es primo. ")


if __name__ == "__main__":
    run()




# def run():
#     numero = int(input("Escribe un número: "))

#     if (numero ** 2) % 2 == 0:
#         print("No es primo.")
#     else:
#         print("Es primo.")


# if __name__ == "__main__":
#     run()