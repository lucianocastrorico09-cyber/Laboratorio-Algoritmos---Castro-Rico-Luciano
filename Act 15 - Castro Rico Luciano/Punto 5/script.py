"""
5. Crear y cargar en un lista los nombres de 5 países y en otra lista paralela
la cantidad de habitantes del mismo. Ordenar alfabéticamente e imprimir
los resultados. Por último ordenar con respecto a la cantidad de habitantes
(de mayor a menor) e imprimir nuevamente.
"""


paises = []
habitantes = []


for x in range(5):

    nombre = input(f"Ingrese el nombre del país {x+1}: ")
    paises.append(nombre)

    cantidad = int(input(f"Ingrese la cantidad de habitantes de {nombre}: "))
    habitantes.append(cantidad)


for i in range(4):

    for j in range(4 - i):

        if paises[j] > paises[j + 1]:

            auxPais = paises[j]
            paises[j] = paises[j + 1]
            paises[j + 1] = auxPais

            auxHab = habitantes[j]
            habitantes[j] = habitantes[j + 1]
            habitantes[j + 1] = auxHab


print("Países ordenados alfabéticamente:")

for x in range(5):
    print(paises[x], habitantes[x])

for i in range(4):


    for j in range(4 - i):


        if habitantes[j] < habitantes[j + 1]:


           
            auxHab = habitantes[j]
            habitantes[j] = habitantes[j + 1]
            habitantes[j + 1] = auxHab


            auxPais = paises[j]
            paises[j] = paises[j + 1]
            paises[j + 1] = auxPais


print("Países ordenados por cantidad de habitantes:")


for x in range(5):
    print(paises[x], habitantes[x])

