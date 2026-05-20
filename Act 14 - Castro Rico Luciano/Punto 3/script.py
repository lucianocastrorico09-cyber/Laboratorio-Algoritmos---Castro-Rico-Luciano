#3. Cargar una lista con 5 elementos enteros. Imprimir el mayor y un mensaje
#si se repite dentro de la lista (es decir si dicho valor se encuentra en 2 o
#más posiciones en la lista)

numeros = []
repetido = 0

for x in range (5):
    valor = int(input(f"Ingrese el valor de la posicion {x+1}: "))
    numeros.append(valor)

mayor = numeros[0]

for x in range (1, 5):
    if numeros[x] > mayor:
        mayor = numeros[x]


print (f"El numero mayor es {mayor}")


for x in range (5): 
    if numeros[x] == mayor:
        repetido += 1



if repetido >= 2:
    print ("Mayor se repite") 