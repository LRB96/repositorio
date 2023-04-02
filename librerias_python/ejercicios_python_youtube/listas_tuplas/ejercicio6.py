materias = ["Matemáticas", "Física", "Historia", "Química"]
for i in range(len(materias) -1,-1,-1):
    nota = float(input(f"¿Qué nota sacaste en {materias[i]}?: "))
    if nota >= 5:
        materias.pop(i)
print(f"Debes repetir {materias}.")














# materias = ["Matemáticas", "Física", "Química", "Historia"]
# for i in range(len(materias)-1,-1,-1):
#     nota = float(input(f"Qué nota sacaste en {materias[i]}: "))
#     if nota >= 5:
#         materias.pop(i)
# print(f"Debes repetir {materias}.")


# def run():
#     my_dict = {i: i**3 for i in range(1,101) if i % 3 != 0}
#     print(my_dict)

# if __name__ == "__main__":
#     run()

#    for i in range(1,101):
#         cube_root = i ** 3
#         if i % 3 != 0:
#             print(str(i) + " elevado al cubo es: " + str(cube_root))