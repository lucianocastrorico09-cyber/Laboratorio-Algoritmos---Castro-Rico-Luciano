"""
3. Confeccionar un programa que permita:
1) Cargar una lista de 10 elementos enteros.
2) Generar dos listas a partir de la primera. En una guardar los valores
positivos y en otra los negativos.
3) Imprimir las dos listas generadas.
"""


def Cargar () :
    for i in range (10):
        l1 = int(input(f"Ingrese el valor numero {i+1} en la lista "))
        lista1.append(l1)

def Generar () :
    for i in range (10):
        if lista1[i] > 0:
            listap.append(lista1[i])
        elif lista1[i] < 0:
            listan.append(lista1[i])


def Imprimir () :
    print ("Lista negativa")
    print (listan)

    print ("Lista positiva")
    print (listap)

lista1 = []
listap = []
listan = []

Cargar()
Generar()
Imprimir()