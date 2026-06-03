"""
4. Plantear una función que reciba un string en mayúsculas o minúsculas y
retorne la cantidad de letras "a" o "A"
"""

def Contar(txt) :
    cantidad1 = txt.count("a")
    cantidad2 = txt.count("A")
    
    cantidad3 = cantidad1+cantidad2
    return cantidad3    


def Pedir_Texto() :

    texto = (input("Ingrese el texto para contar la cantidad "))
    
    print("La cantidad de A que hay son ")

    print(Contar(texto))


Pedir_Texto()