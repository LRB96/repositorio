materias = ["Matemáticas", "Física","Química","Historia"]
notas = []
for materia in materias:
    nota = int(input(f"¿Qué nota sacaste en {materia}?: "))
    notas.append(nota)
for i in range(len(materias)):
    print(f"Tu nota en {materias[i]} fue {notas[i]}.")



# asignaturas = ["Matemáticas", "Inglés", "Física", "Química"]
# notas = []
# for asignatura in asignaturas:
#     nota = input(f"Qué nota sacaste en {asignatura}: ")
#     notas.append(nota)
# for i in range(len(asignaturas)):
#     print(f"La nota en {asignaturas[i]} es: {notas[i]}")