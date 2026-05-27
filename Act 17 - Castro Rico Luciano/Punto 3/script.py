"""
3. Definir una lista y almacenar los nombres de 3 empleados.
Por otro lado definir otra lista y almacenar en cada elemento una sublista con los
números de días del mes que el empleado faltó.
Imprimir los nombres de empleados y los días que faltó.
Mostrar los empleados con la cantidad de inasistencias.
Finalmente mostrar el nombre o los nombres de empleados que faltan menos
días.
"""

nombres = []
inasistencias = []

for x in range(3):
    nombre = input("Ingrese el nombre del empleado ")
    nombres.append(nombre)

    cantidad = int(input(f"Cuantos dias falto el empleado?"))

    faltas = []
    for j in range(cantidad):
        dia = int(input("Ingrese el dia que falto "))
        faltas.append(dia)

    inasistencias.append(faltas)

print("Empleados y dias de inasistencia")
for x in range(3):
    print(nombres[x],"falto los dias", inasistencias[x])

print("Cantidad de inasistencias")
for x in range(3):
    print(nombres[x], "tuvo", len(inasistencias[x]), "inasistencias")

menor = len(inasistencias[0])

for x in range(1, 3):
    if len(inasistencias[x]) < menor:
        menor = len(inasistencias[x])

print("Empleados con menos inasistencias")
for x in range(3):
    if len(inasistencias[x]) == menor:
        print(nombres[x], "con", menor, "inasistencias")
    




