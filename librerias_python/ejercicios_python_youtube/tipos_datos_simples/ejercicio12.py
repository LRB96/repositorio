barras_pan = int(input("¿Cuántas barras de pan, no frescas, hay?: "))
precio_barras = 3.49
descuento = 0.6
costo_final = barras_pan * precio_barras * (1-descuento)

print(f"El precio de una barra de pan es de: {precio_barras}€.")
print(f"El descuento para una barra de pan no fresca es de: {100*descuento}%.")
print(f"El costo final, por {barras_pan} es de: {costo_final}€.")