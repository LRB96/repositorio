def make_division_by(n):
    def division_by(x):
        # assert type(int) == int, "Solo se pueden ingresar numeros."
        return x / n
    return division_by


def run():
    division_by_3 =  make_division_by(3)
    print(round(division_by_3(18)))
    division_by_5 = make_division_by(5)
    print(round(division_by_5(20)))
    division_by_10 = make_division_by(10)
    print(round(division_by_10(100)))


if __name__ == "__main__":
    run()