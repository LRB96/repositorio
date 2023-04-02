from functools import reduce


my_list = [2,2,2,2,2]
all_multiplied = reduce(lambda a, b: a * b, my_list)
print(all_multiplied)



# def run():
#     my_dict = {i: round(i**0.5,2) for i in range(1,1001)}
#     for key, value in my_dict.items():
#         print("La raíz cuadrada de " + str(key) + " es " + str(value))


# if __name__ == "__main__":
#     run()