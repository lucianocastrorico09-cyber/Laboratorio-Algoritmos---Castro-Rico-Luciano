"""
2-
Confeccionar un programa con las siguientes funciones:
1)Cargar el nombre de un empleado y su sueldo. Retornar una tupla con dichos
valores
2)Una función que reciba como parámetro dos tuplas con los nombres y sueldos
de empleados y muestre el nombre del empleado con sueldo mayor.
En el bloque principal del programa llamar dos veces a la función de carga y
seguidamente llamar a la función que muestra el nombre de empleado con sueldo
mayor.
# bloque principal
empleado1=cargar_empleado()
empleado2=cargar_empleado()
mayor_sueldo(empleado1,empleado2)
"""

def Cargar () :
    nombre = input("Ingrese el nombre del empleado ")
    sueldo = int(input("Ingrese el sueldo del empleado "))
    return nombre,sueldo

def mayor(emp1, emp2):
 
    if emp1[1] > emp2[1]:
        print(f"El empleado con mayor sueldo es {emp1[0]} con {emp1[1]}")
    elif emp1[1] < emp2[1]:
        print(f"El empleado con mayor sueldo es {emp2[0]} con {emp2[1]} ")

empleado1 = Cargar()
empleado2 = Cargar()

mayor(empleado1, empleado2)