notas = [9, 6, 8, 4, 10]
for nota in notas:
    if nota >= 7:
        print(nota, "Aprobado")
    else:
        print(nota, "Reprobado")
print("Total de aprobados:", sum(1 for nota in notas if nota >= 7))
print("Total de reprobados:", sum(1 for nota in notas if nota < 7))
print("Total de notas:", len(notas))
# TAREA 1: Mostrar tambien las notas reprobadas con else.
# TAREA 2: Contar aprobados y reprobados.
# TAREA 3: Mostrar ambos totales.
