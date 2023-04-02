puntuacion = float(input("Escribe tu puntuación: "))
sueldo = 2400
beneficio = (puntuacion * sueldo) + sueldo
nivel = ""
if puntuacion == 0 or puntuacion == 0.0:
    nivel = "inaceptable"
    print(f"Tu beneficio es de: ${beneficio} y tienes un nivel {nivel}.")
elif puntuacion == 0.4:
    nivel = "aceptable"
    print(f"Tu beneficio es de: ${beneficio} y tienes un nivel {nivel}.")
elif puntuacion == 0.6:
    nivel = "meritorio"
    print(f"Tu beneficio es de: ${beneficio} y tienes un nivel {nivel}.")
elif puntuacion > 0.6:
    nivel = "excelente"
    print(f"Tu beneficio es de: ${beneficio} y tienes un nivel {nivel}.")