#Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la
#altura promedio de las personas.

n = int(input("Ingrese la cantidad de personas"))
suma= 0

for i in range(0,n,1):
    altura = int(input(f"Ingrese la altura de la persona numero {i+1}"))
    suma= suma+altura
    

promedio= suma/n

print(f"La altura promedio es de {promedio}")