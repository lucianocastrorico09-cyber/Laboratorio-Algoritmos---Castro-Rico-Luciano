"""
2. Desarrollar una aplicación que permita ingresar por teclado los nombres de
5 artículos y sus precios.
Definir las siguientes funciones:
1) Cargar los nombres de artículos y sus precios.
2) Imprimir los nombres y precios.
3) Imprimir el nombre de artículo con un precio mayor
4) Ingresar por teclado un importe y luego mostrar todos los artículos con
un precio menor igual al valor ingresado.
"""

def Cargar () :
    for i in range (5) :
        nom = (input(f"Ingrese el nombre del articulo numero {i+1} "))
        nombres.append(nom)
        pre = int(input(f"Ingrese el precio del producto numero {i+1} "))
        precios.append(pre)


def Imprimir () :
    for i in range (5) :
        print (f"{nombres[i]} {precios[i]}")

def Mayor () :
    
    mayor = precios[0]
    nombre = ""

    for i in range (4) :
        
        if mayor > precios[i+1]:
    
           mayor = precios[i]
           nombre = nombres[i]

    print (f"El producto con mayor precio es {nombre} {mayor}")

def Importe () :
    imp = int(input("Ingrese el importe a cobrar "))
    for i in range (5) :

        if imp >= precios[i]:

            print("Productos con un precio menor o igual al importe")
            print (f"{nombres[i]} {precios[i]}")

nombres = []
precios = []

Cargar()
Imprimir()
Mayor()
Importe()