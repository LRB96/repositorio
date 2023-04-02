while True:
    word = input("Escribe algo: ")
    if word == "salir":
        break
    print(word)


# frase = input("Escribe una frase: ")
# letra = input("Escribe una letra: ")
# contador = 0
# for i in frase:
#     if i == letra:
#         contador += 1
# print(f"La letra {letra} aparece {contador} veces en la frase: {frase}.")


# frase  = input("Escribe una frase: ")
# letra = input("Escribe una letra: ")
# contador = 0
# for i in frase :
#     if i == letra:
#         contador += 1
# print(f"La letra {letra} aparece {contador} veces en la frase.")



# word = input("Escribe una palabra: ")
# for i in range(len(word)-1, -1, -1):
#     print(word[i])

# palabra = input("Escribe una palabra: ")
# palabra = palabra[::-1]
# print(f"{palabra}")

# for i in range(1,101):
#     if i%3 == 0 and i%5 == 0:
#         print(f"{i} es: FizzBuzz")
#     elif i%3 == 0:
#         print(f"{i} es: Fizz")
#     elif i%5 == 0:
#         print(f"{i} es: Buzz")
#     else:
#         print(i)


# def es_palindromo(palabra):
#     palabra = palabra.replace(" ", "")
#     palabra = palabra.lower()
#     palabra_invertida = palabra[::-1]
#     if palabra == palabra_invertida:
#         return True
#     else:
#         return False
   
# def run():
#     palabra = input("Escribe una palabra o frase: ")
#     es_palindromo(palabra)
#     if es_palindromo:
#         print("Es palindromo.")
#     else:
#         print("No es palindromo.")

# if __name__ == "__main__":
#     run()