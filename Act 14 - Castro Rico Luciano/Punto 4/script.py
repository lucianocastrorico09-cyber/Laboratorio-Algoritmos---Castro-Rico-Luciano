#4. Cargar por teclado y almacenar en una lista las alturas de 5 personas
#(valores float)
#Obtener el promedio de las mismas. Contar cuántas personas son más
#altas que el promedio y cuántas más bajas.

alturas = []

for x in range (5):
    valor  = float(input(f"Ingrese la altura de la persona {x+1}"))
    alturas.append(valor)
 
suma = 0

for x in range (5):
    suma += alturas[x]

promedio = suma/5
menor = 0
mayor = 0


for x in range (5): 
    if alturas[x] > promedio:
        mayor += 1

    elif alturas[x] < promedio: 
        menor +=1




print (f"El promedio es de {promedio}")
print (f"Las personas con altura mas baja del promedio son {menor}")
print (f"Las personas con altura mas alta del promedio son {mayor}")