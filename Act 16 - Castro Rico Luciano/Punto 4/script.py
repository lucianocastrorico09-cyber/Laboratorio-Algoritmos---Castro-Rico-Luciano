"""
4. Se realiza una evaluación a 6 docentes por parte de sus alumnos. Se registran
sus nombres y puntajes promedio obtenidos (de 1 a 10).
Cargar sus datos en vectores paralelos, mostrar docente con calificación más
alta y más baja, ordenar los vectores de mayor a menor de acuerdo con la
calificación y mostrar en pantalla la cantidad de docentes que aprobaron y
desaprobaron (tomando como base que se aprueba con una nota mayor o
igual a 6)
"""

nombres = []
puntajes = []

for x in range(6):
    nombre = input(f"Ingrese el nombre del profesor numero {x+1} ")
    puntaje = int(input(f"Ingrese el puntaje del profesor {nombre} "))

    nombres.append(nombre)
    puntajes.append(puntaje)

mayor = puntajes[0]
menor = puntajes[0]

for x in range(6):

    if puntajes[x] > mayor:
        mayor = puntajes[x]

    if puntajes[x] < menor:
        menor = puntajes[x]

print("Docente con calificación más alta:")

for x in range(6):

    if puntajes[x] == mayor:
        print(nombres[x], puntajes[x])

print("Docente con calificación más baja:")

for x in range(6):

    if puntajes[x] == menor:
        print(nombres[x], puntajes[x])


for x in range(6):
    for j in range(x + 1, 6):

        if puntajes[x] < puntajes[j]:

            auxPuntaje = puntajes[x]
            puntajes[x] = puntajes[j]
            puntajes[j] = auxPuntaje

            auxNombre = nombres[x]
            nombres[x] = nombres[j]
            nombres[j] = auxNombre

print("Puntaje ordenado:")

for x in range(6):
    print(nombres[x], puntajes[x])

aprobados = 0
desaprobados = 0

for x in range(6):
    if puntajes[x] >= 6:
        aprobados += 1
    else:
        desaprobados += 1

print(f"Cantidad de aprobados: {aprobados}")
print(f"Cantidad de desabrobados: {desaprobados}")