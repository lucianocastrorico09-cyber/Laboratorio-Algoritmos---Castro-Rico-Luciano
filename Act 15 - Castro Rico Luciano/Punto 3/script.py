"""
3. Solicitar por teclado la cantidad de empleados que tiene la empresa. Crear
y cargar una lista con todos los sueldos de dichos empleados. Imprimir la
lista de sueldos ordenamos de menor a mayor.
"""

n = int(input("Ingrese la cantidad de empleados que tiene la empresa: "))

empleados = []
sueldos = []

for x in range(n):
    em = input(f"Ingrese el nombre del empleado {x+1}: ")
    empleados.append(em)

    sue = int(input(f"Ingrese el sueldo del empleado {x+1}: "))
    sueldos.append(sue)


for k in range(n):

    for x in range(n-1):
        if sueldos[x]> sueldos[x+1]:
            aux1=sueldos[x]
            sueldos[x]=sueldos[x+1]
            sueldos[x+1]=aux1
            
            aux2=empleados[x]
            empleados[x]=empleados[x+1]
            empleados[x+1]=aux2

for x in range(n):
    print(sueldos[x],empleados[x])
