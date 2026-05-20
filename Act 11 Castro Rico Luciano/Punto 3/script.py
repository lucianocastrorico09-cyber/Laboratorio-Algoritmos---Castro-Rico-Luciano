#3. Realizar un programa que solicite la carga por teclado de dos números, si el
#primero es mayor al segundo informar su suma y diferencia, en caso
#contrario informar el producto y la división del primero respecto al segundo.


numero1 = int(input("Ingrese el valor del primer numero"))
numero2 = int(input("Ingrese el valor del segundo numero"))
suma = (numero1+numero2)
diferencia = (numero1-numero2)
producto = (numero2*numero1)
division = (numero2/numero1)


if numero1 > numero2:
    print ("la suma es de ")
    print (suma)
    print ("la diferencia es de ")
    print (diferencia)

else:
    print("el producto es de ")
    print (producto)
    print ("La division es de")
    print (division)


    