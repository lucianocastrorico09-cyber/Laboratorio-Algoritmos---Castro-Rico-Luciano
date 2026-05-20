#4. Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el plano. 
#Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto cuadrante.
#Al comenzar el programa se pide que se ingrese la cantidad de puntos a procesar.

n = int(input("Ingrese la cantidad de puntos: "))

cuadrante1 = 0
cuadrante2 = 0
cuadrante3 = 0
cuadrante4 = 0

for i in range(n):
    print(f"Punto {i+1}")
    x = int(input("Ingrese coordenada x: "))
    y = int(input("Ingrese coordenada y: "))

    if x > 0 and y > 0:
        cuadrante1 += 1
    elif x < 0 and y > 0:
        cuadrante2 += 1
    elif x < 0 and y < 0:
        cuadrante3 += 1
    elif x > 0 and y < 0:
        cuadrante4 += 1

print(f"Primer cuadrante: {cuadrante1}")
print(f"Segundo cuadrante: {cuadrante2}")
print(f"Tercer cuadrante: {cuadrante3}")
print(f"Cuarto cuadrante: {cuadrante4}")