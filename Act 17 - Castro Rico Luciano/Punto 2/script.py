"""
2. Se desea saber la temperatura media trimestral de cuatro países. Para ello se
tiene como dato las temperaturas medias mensuales de dichos países. Se debe
ingresar el nombre del país y seguidamente las tres temperaturas medias
mensuales.
Seleccionar las estructuras de datos adecuadas para el almacenamiento de los
datos en memoria.

● Cargar por teclado los nombres de los países y las temperaturas
medias mensuales.
● Imprimir los nombres de los países y las temperaturas medias
mensuales de las mismas.
● Calcular la temperatura media trimestral de cada país.
● Imprimir los nombres de los países y las temperaturas medias
trimestrales.
● Imprimir el nombre del país con la temperatura media trimestral
mayor.
"""

pais = []
temperaturas = []

for x in range(4):
    paises = input(f"Ingrese el nombre del pais {x+1}: ")
    pais.append(paises)

    temp1 = int(input("Ingrese la temperatura 1 "))
    temp2 = int(input("Ingrese la temperatura 2 "))
    temp3 = int(input("Ingrese la temperatura 3 "))

    temperaturas.append([temp1, temp2, temp3])

print("Temperaturas cargadas:")

for x in range(4):
    print(pais[x], temperaturas[x])

mayor = 0
paismayor = ""

print("Promedios trimestrales:")

for x in range(4):

    suma = temperaturas[x][0] + temperaturas[x][1] + temperaturas[x][2]

    promedio = suma / 3

    print(pais[x], "Promedio", promedio)

    if promedio > mayor:
        mayor = promedio
        paismayor = pais[x]

print(f"Pais con mayor promedio trimestral {paismayor} ")
