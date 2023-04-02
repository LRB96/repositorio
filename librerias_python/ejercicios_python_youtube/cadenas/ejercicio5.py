frase = input("Escribe una frase: ")
frase = frase.lower()
frase = frase.replace(" ","")
frase_invertida = frase[::-1]
if frase == frase_invertida:
    print("Es un palindromo.")
else:
    print("No es un palindromo.")