"""
2. Realizar un programa que pida la carga de dos listas numéricas enteras
de 4 elementos cada una. Generar una tercera lista que surja de la suma
de los elementos de la misma posición de cada lista. Mostrar esta tercera
lista.

"""

lista1 = []
lista2 = []
lista3 = []


for x in range (4) :
    l1 = int (input(f"Ingrese el valor numero {x+1} en la lista 1 "))
    lista1.append(l1)
    l2 = int (input(f"Ingrese el valor numero {x+1} en la lista 2 "))
    lista2.append(l2)
 
for x in range (4) :
    l3 = lista1[x] + lista2[x]
    lista3.append(l3)



print (lista3)