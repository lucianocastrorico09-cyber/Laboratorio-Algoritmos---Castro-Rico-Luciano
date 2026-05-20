#4. Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
#a. La cantidad de valores ingresados negativos.
#b. La cantidad de valores ingresados positivos.
#c. La cantidad de múltiplos de 15.
#d. El valor acumulado de los números ingresados que son pares.


negativos = 0
positivos = 0
multiplos15 = 0
suma_pares = 0


for i in range(10):
    num = int(input(f"Ingrese numero el numero {i+1} "))

    if num < 0:
        negativos += 1
    elif num > 0:
        positivos += 1

    if num % 15 == 0:
        multiplos15 += 1

    if num % 2 == 0:
        suma_pares += num

    i += 1

print("Negativos ", negativos)
print("Positivos ", positivos)
print("Multiplos de 15 ", multiplos15)
print("Suma de pares ", suma_pares)