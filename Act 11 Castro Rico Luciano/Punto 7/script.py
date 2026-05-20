#7. Escribir un programa en el cual: dada una lista de tres valores numéricos
#distintos se calcule e informe su rango de variación (debe mostrar el mayor
#y el menor de ellos)

numero1 = int(input("Ingrese el numero 1 "))
numero2 = int(input("Ingrese el numero 2 "))
numero3 = int(input("Ingrese el numero 3 "))
menor = numero1
mayor = numero1


if numero2 > mayor:
    mayor = numero2
if numero3 > mayor:
    mayor = numero3

if numero2 < menor:
    menor = numero2
if numero3 < menor:
    menor = numero3

print("El numero mayor es:", mayor)
print("El numero menor es:", menor)