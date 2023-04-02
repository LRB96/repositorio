name = input("¿Cuál es tu nombre?: ")
sex = input("¿Qué sexo eres? (M o H): ")
if sex == "M":
    if name.lower() < "m":
        grupo = "A"
    else:
        grupo = "B"
else:
    if name.lower() > "n":
        grupo = "A"
    else:
        grupo = "B"
print(f"Tu grupo es el: {grupo}.")