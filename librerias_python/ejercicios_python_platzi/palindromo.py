#Función inicializadora
#Función principal run()
#En la función principal creo 2 variables
#La primera variable "palabra", en la cual guardo la palabra que le pido al usuario con input.
#La segunda variable "es_palindromo", en la cual guardo lo que me retorna la función palindromo, y a la cual le paso como parámetro la variable "palabra"
#Creo una condición: if es_palindromo == true print("Es palindromo"), else: print("No es palindromo")

#En la función palindromo el parámetro palabra es una variable a la cual se le quitan los espacios vacios con .replace(" ", "")
#Después se convierten todos los elementos en miniscula, con .lower()
#Se le da vuelta con [::-1], para que se verifique que es un palindromo}. Todo esto en una variable: palabra_invertida
#if palabra_invertida == palabra:
#     retrun True
#Else:
#    return False



def palindromo(palabra):
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra_invertida == palabra:
        return True
    else: 
        return False


def run():
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es palindromo.")
    else:
        print("No es palindromo.")
    

if __name__ ==  "__main__":
    run()