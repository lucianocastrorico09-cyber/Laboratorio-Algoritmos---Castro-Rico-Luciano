#2. Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8
#empleados (4 por la mañana y 4 por la tarde) Confeccionar un programa
#que permita almacenar los sueldos de los empleados agrupados en dos
#listas. Imprimir las dos listas de sueldos.


mañana =    []
tarde =     []

for x in range (5) :
    numeroM = int(input(f"Ingrese el sueldo de la persona de la mañana {x+1} "))
    mañana.append(numeroM)

    numeroT = int(input(f"Ingrese el sueldo de la persona de la tarde {x+1} "))
    tarde.append(numeroT)
    

print (f"Turno mañana: {mañana}")
print (f"Turno tarde: {tarde}")