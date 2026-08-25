"""
4-
Un comercio de tecnología necesita administrar el stock de sus 5 componentes clave de
hardware.
 Crear una lista donde cada elemento sea una tupla de tres elementos que
represente: (nombre_articulo, precio, stock).
Desarrollar las siguientes funciones:
1. Cargar inventario: Ingresar por teclado los datos de los 5 componentes para
armar las tuplas correspondientes.
2. Imprimir listado: Mostrar por pantalla los nombres, precios y stock de todos los
artículos desempaquetando la tupla de manera directa en el bucle for.
3. Valor del Inventario: Calcular e informar el valor total de la mercadería en el local
(sumando el resultado de precio * stock de cada uno de los componentes).
4. Alerta de Reposición: Imprimir el nombre de todos aquellos artículos cuyo stock
sea menor o igual a 10 unidades para emitir un aviso de compra urgente.
"""

def cargar():
    productos = []

    for i in range(5):
        nombre = input(f"Ingrese el nombre del producto ")
        precio = int(input(f"Ingrese el precio del producto "))
        stock = int(input("Ingrese el stock del producto "))
        productos.append((nombre,precio,stock))

    return productos

def desempaquetar(productos):
    for nombre,precio,stock in productos:
        print(f"{nombre} {precio}$ {stock} unidades")


def calcular_total(productos):
    total = 0

    for nombre, precio, stock in productos:
        total += precio * stock

    print(f"Valor total del inventario: ${total}")
            

def alerta(productos):
     for nombre,precio,stock in productos:
          if stock <=10:
               print (f"ALERTA menos de 10 unidades en stock ({nombre}), reponer urgentemente")


productos = cargar()
desempaquetar(productos)
calcular_total(productos)
alerta(productos)