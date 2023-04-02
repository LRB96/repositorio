fecha = input("Escribe tu fecha de nacimiento en formato dd/mm/aaaa: ")
dia = fecha[:fecha.find('/')]
mesano = fecha[fecha.find('/')+1:]
mes = mesano[:mesano.find('/')]
ano = mesano[mesano.find('/')+1:]

print("Día", dia)
print("Mes", mes)
print("Año" , ano)