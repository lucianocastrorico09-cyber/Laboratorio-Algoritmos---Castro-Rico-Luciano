"""
1. En un curso de 4 alumnos se registraron las notas de sus exámenes y se
deben procesar de acuerdo a lo siguiente:
a. Ingresar nombre y nota de cada alumno (almacenar los datos en
dos listas paralelas)
b. Realizar un listado que muestre los nombres, notas y condición del
alumno. En la condición, colocar "Muy Bueno" si la nota es mayor o
igual a 8, "Bueno" si la nota está entre 4 y 7, y colocar "Insuficiente";
si la nota es inferior a 4.
c. Imprimir cuántos alumnos tienen la leyenda “Muy Bueno”.
"""
nombre = []
nota = []
cantidad = 0

for x in range (4) :
    nom= input(f"Ingrese el nombre del alumno numero {x+1} ")
    nombre.append(nom)
    notas= int(input("Ingrese la nota del alumno"))
    nota.append(notas)



for x in range (4) :

    if nota[x] >= 8 :
     print (f"Alumno {nombre[x]} {nota[x]} Muy bueno ")
     cantidad += 1
    
    elif nota[x] >= 4 and nota[x] <= 7 :
       
       print (f"Alumno {nombre[x]} {nota[x]} Bueno")

    else:
        print (f"Alumno {nombre[x]} {nota[x]} Insuficiente")


print (f"Hay un total de {cantidad} alumnos con Muy bueno")
