"""

3. Confeccionar una función que calcule la superficie de un rectángulo y la
retorne, la función recibe como parámetros los valores de dos de sus lados:
def retornar_superficie(lado1,lado2):
En el bloque principal del programa cargar los lados de dos rectángulos y
luego mostrar cuál de los dos tiene una superficie mayor.

"""
superficie = 0

def Calcular (l1,l2) :

    superficie = l1*l2

    return superficie
    

def Pedir_Numeros() :

    lado1= int(input("Ingrese el lado 1 "))

    lado2= int(input("Ingrese el lado 2 "))
    
    print (f"La superficie es de")
    print (Calcular(lado1,lado2))
    
    if lado1 > lado2 :
        print (f"El lado mayor es el de {lado1}")
    else: 
        print (f"El lado mayor es el de {lado2}")



Pedir_Numeros()