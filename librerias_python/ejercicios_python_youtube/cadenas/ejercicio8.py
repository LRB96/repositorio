precio = input("Escribe un precio con 2 decimales: ")
print(f"El precio es de: {precio[:precio.find('.')]} Euros con {precio[precio.find('.')+1:]} céntavos.")