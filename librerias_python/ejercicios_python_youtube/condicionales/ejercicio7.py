renta = float(input("¿Cuánto ganas al año?: "))
if renta < 10000:
    tipo_impositivo = 5
elif renta < 20000:
    tipo_impositivo = 15
elif renta < 35000:
    tipo_impositivo = 20
elif renta < 60000:
    tipo_impositivo = 30
else:
    tipo_impositivo = 40
print(f"Tienes que pagar: {renta * tipo_impositivo / 100}€.")