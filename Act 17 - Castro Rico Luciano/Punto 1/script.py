"""
1. Se tiene la siguiente lista:
lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]
Imprimir la lista. Luego fijar con el valor cero todos los elementos mayores a 50
del primer elemento de &quot;lista&quot;.
Volver a imprimir la lista.
"""

lista = [[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]

print(lista)

primera = []

for x in range(len(lista)):
    
    nuevaLista = []
    
    for j in lista[x]:
        
        if j > 50:
            primera.append(j)
        else:
            nuevaLista.append(j)
    
    lista[x] = nuevaLista

lista[0] = primera

print(lista)