"""
4. Elaborar una función que muestre la tabla de multiplicar del valor que le
enviemos como parámetro. Definir un segundo parámetro llamado termino
que por defecto almacene el valor 10. Se deben mostrar tantos términos de
la tabla de multiplicar como lo indica el segundo parámetro.
Llamar a la función desde el bloque principal de nuestro programa con
argumentos nombrados.
"""

def multiplicar (numero,termino=10):

    for x in range (1, termino+1):
        print (numero*x)




num = int(input("Ingrese el numero a multiplicar "))
term = int(input("Ingrese la cantidad de veces que quiere que se multiplique (Si no pone nada es 10) "))


multiplicar(num,term)