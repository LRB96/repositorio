def bohemian(func):
    def rapsody(text):
        return func(text) * 5
    return rapsody


@bohemian
def queen(name: str):
    return f"{name}"


print(queen("Galileo ") + f"Figaro " + " " + "Magnificoooo!")



# def mayusculas(func):
#     def envoltura(texto):
#         return func(texto).upper()
#     return envoltura

# @mayusculas
# def mensaje(nombre: str):
#     return f"{nombre}, recibiste un mensaje"


# print(mensaje("César"))




# from datetime import datetime

# def execution_time(func):
#     def wrapper(*args, **kwargs):
#         initial_time = datetime.now()
#         func(*args, **kwargs)
#         final_time = datetime.now()
#         total_time = final_time - initial_time
#         print("Pasaron " + str(total_time.total_seconds()) + " segundos.")
#         return wrapper
        

# def run():
#     for _ in range(1, 1000):
#         pass


# @execution_time
# def suma(a: int, b: int) -> int:
#     return a + b

# print(suma(5,5))
