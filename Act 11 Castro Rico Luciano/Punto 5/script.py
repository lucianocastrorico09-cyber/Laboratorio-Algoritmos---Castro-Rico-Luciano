#Se ingresa por teclado un valor entero, mostrar una leyenda que indique si
#el número es positivo, negativo o nulo (es decir cero)

numero = int(input(("Ingrese el numero")))

if numero < 0: 
    print ("El numero es negativo")
else:
        if numero > 0:
              print  ("El numero es positivo")
        else:
              if numero == 0:
                print("El numero es nulo")
              