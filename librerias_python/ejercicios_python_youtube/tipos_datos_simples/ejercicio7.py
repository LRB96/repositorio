peso = float(input("Escribe tu peso en kilos: "))
altura = float(input("Escribe tu altura en centímetros: "))
imc = peso / altura**2

print(f"Tu índice de masa corporal es {round(imc,2)}")