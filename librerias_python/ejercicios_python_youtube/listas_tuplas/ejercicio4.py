numeros_ganadores = []
for i in range(6):
    numero = int(input("Escribe un número menor o igual a 49: "))
    if numero <= 49:
        numeros_ganadores.append(numero)
print(f"Los números ganadores son: {numeros_ganadores}.")








# numeros_ganadores = []
# for i in range(6):
#     numeros_ganadores.append(int(input("Escribe un número ganador: ")))
#     numeros_ganadores.sort()
# print(f"Los números ganadores son: {numeros_ganadores}")


# raise Exception (f"El valor ingresado no es válido." , "\n", "Escribe un número válido.")