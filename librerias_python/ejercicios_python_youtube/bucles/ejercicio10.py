n = int(input("Escribe un número entero: "))
for i in range(2,n):
    if n % i == 0:
        break
if (i + 1)  == n:
    print(str(n) + " es primo")
else: 
    print(str(n) + " no es primo")