#1. Escribir un programa que solicite ingresar 10 notas de alumnos y nos
#informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.
mayor = 0
menor = 0


for i in range(10):
    nota = int(input(f"Ingrese la nota del alumno numero {i+1} "))
    if nota >= 7:
        mayor = mayor+1
    else:
        if nota < 7:
            menor = menor+1



print ("La cantidad de alumnos con notas mayores a 7 es de ")
print (mayor)
print ("La cantidad de alumnos con notas menores a 7 es de ")
print (menor)