"""
4. Cargar una lista con 5 elementos enteros. Ordenar de menor a mayor y
mostrarla por pantalla, luego ordenar de mayor a menor e imprimir
nuevamente.
"""

lista = []

for x in range(5):
    valor = int(input(f"Ingrese el valor numero {x+1} "))
    lista.append(valor)


for j in range(4):
    for i in range(4):

        if lista[i] > lista[i + 1]:
            aux = lista[i]
            lista[i] = lista[i + 1]
            lista[i + 1] = aux


print("Lista ordenada de menor a mayor:")
print(lista)


for i in range(4):

    for j in range(4):
        
        if lista[j] < lista[j + 1]:

            aux = lista[j]
            lista[j] = lista[j + 1]
            lista[j + 1] = aux


print("Lista ordenada de mayor a menor:")
print(lista)
