"""
5-
Almacenar los nombres de 5 productos y sus precios. Utilizar una lista y cada
elemento una tupla con el nombre y el precio.
Desarrollar las funciones:
1) Cargar por teclado.
2) Listar los productos y precios.
3) Imprimir los productos con precios comprendidos entre 10 y 15.
"""

def carga():
    productos=[]
    for i in range(5):
        nombr=input(f"Ingrese el nombre del producto {i+1} ")
        preci=[]
        for x in range(1):
            if x==0:
                precio=int(input(f"Ingrese el precio de el producto {nombr} "))
                preci.append(precio)      
        tupla=tuple(preci)
        productos.append([nombr,tupla])
    return productos

def imprimir(productos):
    print("Los productos con un precio comprendido entre 10 y 15 son ")
    for i in range(5):
        if productos[i][1][0] >= 10 and productos[i][1][0]<=15:
            print(f"El producto {productos[i][0]} con un precio de {productos[i][1][0]}")


productos=carga()
imprimir(productos)