from cgi import print_arguments


edad = int(input("¿Cuál es tu edad?: "))
if edad < 4:
    print("Puedes entrar gratis.")
elif edad == 4 or edad <= 18:
    print("Tienes que pagar 5€.")
else:
    print("Tienes que pagar 10€.")