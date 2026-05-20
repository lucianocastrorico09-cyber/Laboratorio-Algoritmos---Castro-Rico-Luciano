#4. Se ingresa por teclado un número positivo de uno o dos dígitos (1..99)
#mostrar un mensaje indicando si el número tiene uno o dos dígitos.
#(Tener en cuenta que condición debe cumplirse para tener dos dígitos un
#número entero)

numero = int(input("Ingrese el numero (de 1 a 99)"))

if numero >= 1 and numero <= 9:

    print ("El numero tiene un digito")

else:
    
    if  numero >= 10 and numero <= 99: 

        print ("El numero tiene dos digitos")

    else:

        print ("Numero fuera de rango") 
