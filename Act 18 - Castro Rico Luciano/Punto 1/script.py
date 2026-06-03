""" 
1. Desarrollar un programa que solicite la carga de tres valores y muestre el
menor. Desde el bloque principal del programa llamar 2 veces a dicha
función (sin utilizar una estructura repetitiva)

"""

def devolver_menor () :
 
 
    n1 = int (input("Ingrese el valor numero 1 "))
    n2 = int (input("Ingrese el valor numero 2 "))
    n3 = int (input("Ingrese el valor numero 3 "))
 
    menor = n1

    if n2 < menor:
      menor = n2
    else: 
        if n3 < menor :
            menor = n3 
   
    return menor

print (devolver_menor ())


print (devolver_menor ())