"""
1-
Confeccionar un programa con las siguientes funciones:
1)Cargar una lista de 5 enteros.
2)Retornar el mayor y menor valor de la lista mediante una tupla.
Desempaquetar la tupla en el bloque principal y mostrar el mayor y menor.
"""


def cargar():
    lista=[]
    for i in range(5):
        lis=int(input(F"Ingrese el entero en la posicion numero {i+1} "))
        lista.append(lis)
    return lista
   
def mayor(lista):
    mayor=lista[0]
    for i in range(5):
        for elemento in lista:
            if elemento >mayor:
                mayor=elemento
    print(F"El mayor elemento de la lista es {mayor} ")
   
def menor(lista):
    menor=lista[0]
    for i in range(5):
        for elemento in lista:
            if elemento <menor:
                menor=elemento
    print(F"El menor elemento de la lista es {menor} ")
   
   
lista=cargar()
mayor(lista)
menor(lista)
