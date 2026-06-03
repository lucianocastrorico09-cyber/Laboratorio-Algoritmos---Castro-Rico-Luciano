""" 

2. Confeccionar una función que reciba tres enteros y los muestre ordenados
de menor a mayor. En otra función solicitar la carga de 3 enteros por
teclado y proceder a llamar a la primer función definida.

"""    

def Ordenar(valor1,valor2,valor3) :
   
   
    if valor1 < valor2 and valor1 < valor3 and valor2 > valor3:
        print (valor1,valor3,valor2)
    else:
        if valor2 < valor1 and valor2 < valor3 and valor1 > valor3:
            print (valor2,valor3,valor1)
        elif valor3 < valor1 and valor3 < valor2 and valor2 > valor1:
             print (valor3,valor1,valor2)
        elif valor1 < valor2 and valor1 < valor3 and valor2 < valor3:
             print(valor1,valor2,valor3)
        elif valor2 < valor1 and valor2 < valor3 and valor1 < valor3:
             print (valor2,valor1,valor3)
        elif valor3 < valor1 and valor3 < valor2 and valor2 < valor1:
             print (valor3,valor2,valor1)




def Pedir_Numeros() :
    v1 = int(input("Ingrese el valor uno "))
    v2 = int(input("Ingrese el valor dos "))
    v3 = int(input("Ingrese el valor tres "))
    
    Ordenar(v1,v2,v3)    
    


Pedir_Numeros()