"""
4. Confeccionar una función que reciba una serie de edades y me retorne la
cantidad que son mayores o iguales a 18 (como mínimo se envía un entero
a la función)
"""

def pedir_edades () :

    for i in range (n) :
        edad=int(input(f"Ingrese la edad numero {i+1} "))
        edades.append(edad)

def controlar() :
    cantidad = 0
    for i in range(n) :
        if edades[i] >= 18:
            cantidad+=1

    print(f"La cantidad de personas mayores o iguales a 18 años son {cantidad}")



n = int(input("Ingrese la cantidad de edades que quiere controlar (minimo 1) "))
edades=[]

pedir_edades()
controlar()