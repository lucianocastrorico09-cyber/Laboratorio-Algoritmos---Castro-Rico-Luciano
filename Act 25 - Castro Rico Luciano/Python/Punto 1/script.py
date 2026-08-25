"""
Confeccionar un programa que permita registrar las temperaturas máximas de las últimas
6 horas en una lista.
Desarrollar las siguientes funciones:
1. Carga: Solicitar al operador el ingreso por teclado de las 6 temperaturas y
almacenarlas en una lista.
2. Procesar Extremos: Recibir la lista como parámetro y retornar una tupla que
contenga en su primer componente el valor máximo y en el segundo el valor
mínimo.
3. Bloque Principal: Desempaquetar la tupla devuelta por la función anterior en dos
variables individuales (máxima y mínima) y mostrarlas en pantalla con un mensaje
descriptivo.
"""

def cargar():
    temp = []
    for i in range(6):
        grados = int(input(f"Ingrese la temperatura numero {i+1} " ))
        temp.append(grados)


    return temp

def extremos(temp):
    for i in range(5):
        if temp[i] > temp[i+1]:
            aux = temp[i]
            temp[i] = temp[i+1]
            temp[i+1] = aux

    return(temp)

def desempaquetado (tempe):
    mayor = tempe[5]
    menor = tempe[0]

    print (f"la temperaturas maximas y minimas son: {mayor},{menor}")
   
       

temperatura = cargar()
extremos(temperatura)
desempaquetado(temperatura)