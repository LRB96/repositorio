cantidad = float(input("Cantidad a invertir: "))
interes = float(input("Tasa de interés: "))
anios = int(input("Años a invertir: "))
for i in range(anios):
    cantidad = cantidad * (1 + interes) ** anios
    if i < 1:
        print(f"La cantidad de dinero después de {i+1} año es de: {round(cantidad,2)}")
    elif i == 1:
        print(f"La cantidad de dinero después de {i+1} años es de: {round(cantidad,2)}")
    elif i > 1:
        print(f"La cantidad de dinero después de {i+1} años es de: {round(cantidad,2)}")
