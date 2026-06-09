"""
2. En una empresa se almacenaron los sueldos de 10 personas.
Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
1) Carga de los sueldos en una lista.
2) Impresión de todos los sueldos.
3) Cuántos tienen un sueldo superior a $4000.
4) Retornar el promedio de los sueldos.
5) Mostrar todos los sueldos que están por debajo del promedio.
"""
sueldos = []

def cargar () :

    for i in range (10) :
        sul = int(input(f"Ingrese el sueldo numero {i+1} "))
        sueldos.append(sul)


def imprimir () :

    print(sueldos)

def calcular () :
    total = 0
    for i in range (10) :
        if sueldos[i] > 4000 :
            total=total+1
    print (f"La cantidad de sueldos que son mayores a 4000 {total}")

def promedio () :
    suma = 0
    for i in range (10) :
        suma+=sueldos[i]
    return suma/10


def menor () :
    for i in range (10) :
        if sueldos[i] < promedio():
            print(f"Sueldos menores al promedio {sueldos[i]}")


cargar()
imprimir()
calcular()
print(f"El promedio de sueldo es {promedio()}")
menor ()