"""
1. Se desea desarrollar un programa que permita registrar los nombres y las
calificaciones de 6 estudiantes. Luego de cargar los datos, se debe mostrar el
nombre del estudiante con la nota más alta, junto con su nota. Al igual que el
estudiante con la nota más baja. Informar si hay estudiantes con la misma nota
máxima o mínima.
"""

estudiantes = []
notas = []
alumno1 = []
alumno2 = []

for i in range(6):
    nombre = input("Ingrese el nombre del estudiante ")
    nota = int(input("Ingrese la calificacion del estudiante "))
    estudiantes.append(nombre)
    notas.append(nota)


maxima = notas[0]
minima = notas[0]

for x in range(6):
    if notas[x] > maxima:
        maxima = notas[x]

    if notas[x] < minima:
        minima = notas[x]

print("Estudiante con nota ms alta ")
for x in range(6):
    if notas[x] == maxima:
        print(estudiantes[x], notas[x])

print("Estudiante con nota mas baja ")
for x in range(6):
    if notas[x] == minima:
        print(estudiantes[x], notas[x])