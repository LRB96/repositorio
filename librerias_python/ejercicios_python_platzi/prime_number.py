def prime_number(number: int):
    if number%2 == 0:
        print("No es primo.")
    else:
        print("Es primo.")


def run():
    print(prime_number(5))


if __name__ == "__main__":
    run()