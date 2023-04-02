#import Random
#Función inicializadora
#Función principal con variable contrasena que guarda el return de la función generar_contrasena
#Print("Tu nueva contraseña es " + contrasena)

#Función generar_contrasena 
# listas para inputs para crear la contraseña 
#Se guardan todas las listas en una variable "caracteres"
#Se guarda una lista vacia en una variable "contrasena"
#Se crea un ciclo for con range(15), es decir, la longitud máxima de la contraseña
#Se usa el módulo random , importado al principio, con random.choice(caracteres), y se guarda en una variable caracter_random, por que va a guardar
#un elemento en cada iteración del total de 15.
#Se agrega cada uno de esos 15 caracteres con contrasena.append(caracter_random) en la lista vacia de la varaible "contrasena"
#Para converitir la lista de los 15 caracteres a un string, se usa contrasena = "".join(contrasena). Esto por que hay que recordar que contrasena es una lista.
#Por último, Return contrasena, para se guarde en la variable contrasena de la función run, y se muestre con print("Tu nueva contraseña es " + contraasena)

import random

def generar_contrasena():
    MAYUS =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    caracteres = MAYUS + MINUS + NUMS + CHARS
    contrasena = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)

    contrasena = "".join(contrasena)
    return contrasena
    



def run():
    contrasena = generar_contrasena()
    print("Tu nueva contraseña es " + contrasena)

if __name__ == "__main__":
    run()
# import random



# def password_generator():
    # mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    # minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    # simbolos = ['!', '#', '$', '&', '/', '(', ')']
    # numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

#     characters = MAYUS + MINUS + NUMS + CHARS
    
#     password = []

#     for i in range(15):
#         random_character = random.choice(characters)
#         password.append(random_character)
    
#     password = "".join(password)
#     return password



# def run():
#     password = password_generator()
#     print("Tu nueva contraseña es: " + password)



# if __name__ == "__main__":
#     run()
