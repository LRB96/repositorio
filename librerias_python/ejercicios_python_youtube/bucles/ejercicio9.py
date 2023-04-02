password = input("Escribe una contraseña: ")
contrasena = "Tesla"
while password != contrasena:
    intento = input("Incorrecto. Intenta de nuevo: ")
    if intento == contrasena:
        input("Bienvenido.")
        break