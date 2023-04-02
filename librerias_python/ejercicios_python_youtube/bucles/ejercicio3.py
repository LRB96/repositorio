num = int(input("Escribe un número entero: "))
print(f"Los números impares desde 1 hasta {num} son:" + "\n")

for i in range(1, num+1, 2):
        print(i, end=",")