"""
1. Desarrollar una función que reciba una lista de string y nos retorne el que
tiene más caracteres. Si hay más de uno con dicha cantidad de caracteres
debe retornar el que tiene un valor de componente más baja.
En el bloque principal iniciamos por asignación la lista de string:
palabras=["enero", "febrero", "marzo", "abril", "mayo", "junio"]
print("Palabra con mas caracteres",mascaracteres(palabras))
(La lista debe tener la misma cantidad de elementos, pero los textos los
eligen ustedes)
"""


def mascaracteres (palabra) :

    for x in range(5) :

        mayor = palabra[0]
        
        if len(mayor) > len(palabra[x+1]):

            mayor = palabra[x]

    return mayor



lista=["Automovil","Perro","Gato","Television","Computadora","Teclado"]

print(f"Palabra con mas caracteres {mascaracteres(lista)}")