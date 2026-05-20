#3. Realizar un programa que permita cargar dos listas de 15 valores cada una. 
#Informar con un mensaje cuál de las dos listas tiene un valor acumulado mayor 
#(mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales") 
#Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.

sumaLista1 = 0
sumaLista2 = 0

print("Cargar valor de la lista 1")
for x in range(15):
    valor1 = int(input(f"Ingrese el valor {x+1}: "))
    sumaLista1 += valor1

print("Cargar valor de la lista 2")
for x in range(15):
    valor2 = int(input(f"Ingrese el valor {x+1}: "))
    sumaLista2 += valor2

if sumaLista1 > sumaLista2:
    print("Lista 1 mayor")

elif sumaLista2 > sumaLista1:
    print("Lista 2 mayor")

else:
    print("Listas iguales")