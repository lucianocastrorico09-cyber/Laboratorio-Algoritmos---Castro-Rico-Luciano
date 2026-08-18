"""4-
Una empresa de e-commerce utiliza drones autónomos para realizar entregas a domicilio
y necesita rastrear las coordenadas geográficas de sus rutas de vuelo.
 Diseñar un diccionario donde la Clave sea el identificador único del dron (ej:
&quot;DRON-01&quot;) y el Valor sea una lista de tuplas que almacene las coordenadas de
las paradas programadas: [(latitud, longitud)].
Desarrollar las siguientes funciones:
1. Cargar planes de vuelo: Ingresar la información de 3 drones. Solicitar para cada
uno la cantidad de paradas que va a realizar y cargar sus respectivas coordenadas
geográficas.
2. Imprimir rutas: Mostrar el listado completo de los drones junto con sus paradas
de coordenadas asociadas.
3. Ruta más larga: Determinar y mostrar el identificador del dron que tiene la mayor
cantidad de paradas registradas en su ruta de vuelo (la lista con mayor cantidad
de elementos)."""

def cargar_vuelos():
    rutas = {}

    for i in range(3):
        codigo_dron = input(f"Ingrese el identificador del dron {i+1}: ")
        coordenadas = []

        total_paradas = int(input("Ingrese la cantidad de paradas: "))

        for j in range(total_paradas):
            lat = float(input("Ingrese la latitud: "))
            lon = float(input("Ingrese la longitud: "))

            coordenadas.append((lat, lon))

        rutas[codigo_dron] = coordenadas

    return rutas


def mostrar_rutas(rutas):
    print("Listado de rutas:")

    for codigo, coordenadas in rutas.items():
        print(f"Dron: {codigo}")

        for lat, lon in coordenadas:
            print(f"  Latitud: {lat} - Longitud: {lon}")


def buscar_ruta_larga(rutas):
    cantidad_mayor = 0
    codigo_mayor = ""

    for codigo, coordenadas in rutas.items():
        if len(coordenadas) > cantidad_mayor:
            cantidad_mayor = len(coordenadas)
            codigo_mayor = codigo

    print(f"El dron con la ruta más larga es: {codigo_mayor}")
    print(f"Cantidad de paradas: {cantidad_mayor}")


rutas = cargar_vuelos()
mostrar_rutas(rutas)
buscar_ruta_larga(rutas)