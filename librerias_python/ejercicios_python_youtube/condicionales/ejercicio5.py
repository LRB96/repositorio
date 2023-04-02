edad = int(input("Escribe tu edad: "))
ingresos_mensuales = int(input("¿De cuánto son tus ingresos mensuales: "))
if edad >= 16 and ingresos_mensuales >= 1000:
    print("Tienes que tributar.")
else:
    print("No tienes que tributar.")