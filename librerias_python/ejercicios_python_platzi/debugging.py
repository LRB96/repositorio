def divisor(num):
    divisors =  []
    for i in range(1, num +1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    num = input("Escribe un número: ")
    assert num.isnumeric() and int(num) > 0, "Debes escribir solo números positivos."
    print("Los divisores de " + num + " son: ")
    print(divisor(int(num)))
    # divisores = "".join(divisor(num))
    # print(divisores)


if __name__ == "__main__":
    run()







# def divisor(num):
#     try:
#         if num < 0:
#             raise ValueError("Escribe un número positivo. ")
#         divisors = []
#         for i in range(1, num + 1):
#             if num % i == 0:
#                 divisors.append(i)
#         return divisors
#     except ValueError as ve:
#         print(ve)
#         return False


# def run():
#     try: 
#         num = int(input("Escribe un número. "))
#         print(divisor(num))
#     except ValueError:
#         print("Debes escribir un número ")


# if __name__ == "__main__":
#     run()