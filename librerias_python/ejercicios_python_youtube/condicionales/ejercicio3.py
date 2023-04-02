numerador = float(input("Escribe un número, entero o decimal: "))
denominador = float(input("Escribe otro número, entero o decimal: "))
if  denominador == 0:
    print("No se puede dividir por 0.")
else:
    print(f"{numerador} dividido entre {denominador} da igual a: {round(numerador/denominador,2)}")