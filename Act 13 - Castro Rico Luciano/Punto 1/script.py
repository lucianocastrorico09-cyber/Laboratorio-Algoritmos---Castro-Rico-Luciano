#1. En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500,   
#realizar un programa que lea los sueldos que cobra cada empleado e informe 
#cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300. 
#Además el programa deberá informar el importe que gasta la empresa en sueldos al personal.



n = int(input("Ingrese la cantidad de empleados: ")) 
    
entre100300 = 0
mas300 = 0
totalsueldos = 0

for i in range(n):
    sueldo = int(input(f"Ingrese el sueldo del empleado {i+1}: "))
    
    totalsueldos += sueldo

    if 100 <= sueldo <= 300:
        entre100300 += 1
    elif sueldo > 300:
        mas300 += 1

print(f"Empleados que cobran entre $100 y $300: {entre100300}")
print(f"Empleados que cobran más de $300: {mas300}")
print(f"Total que gasta la empresa en sueldos: ${totalsueldos}")


