"""
2. Una empresa registra los nombres de sus 5 vendedores y el total de ventas
realizadas por cada uno en un mes. Cargar los nombres y ventas en dos
vectores paralelos, ordenar los datos de mayor a menor según las ventas,
imprimir la lista ordenada con nombre y monto de la venta, e informar quien fue
el que menos vendió de los 5 empleados.
"""
nombres = []
ventas = []

for x in range(5):
    nombre = input("Ingrese el nombre del vendedor: ")
    venta = int(input("Ingrese la cantidad de ventas por mes del vendedor: "))
    
    nombres.append(nombre)
    ventas.append(venta)

for j in range(4):
    for k in range(4 - j):
        if ventas[k] < ventas[k + 1]:

            aux1 = ventas[k]
            ventas[k] = ventas[k + 1]
            ventas[k + 1] = aux1

            aux2 = nombres[k]
            nombres[k] = nombres[k + 1]
            nombres[k + 1] = aux2

print("Lista ordenada de mayor a menor")

for x in range(5):
    print(nombres[x], ventas[x])

print(f"El empleado que menos vendió fue {nombres[4]}")