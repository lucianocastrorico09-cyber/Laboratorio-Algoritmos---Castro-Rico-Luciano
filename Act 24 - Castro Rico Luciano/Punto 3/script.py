"""3-
Un sistema de hogar inteligente monitorea qué electrodomésticos consumen más energía
en cada habitación de la casa.
 Crear un diccionario donde la Clave sea el nombre del ambiente (ej: &quot;Cocina&quot;,
&quot;Dormitorio&quot;) y el Valor sea una lista de tuplas, donde cada tupla represente un
dispositivo activo y su consumo: [(nombre_dispositivo, consumo_watts)].
Desarrollar las siguientes funciones:
1. Cargar dispositivos: Solicitar la carga de 3 habitaciones. Para cada habitación,
ingresar el nombre de los dispositivos activos y su consumo en Watts hasta que el
operador decida no cargar más para ese ambiente.
2. Consumo por habitación: Imprimir el listado de habitaciones y el consumo total
en Watts acumulado en cada una de ellas.
3. Dispositivo crítico: Buscar e informar el nombre del electrodoméstico que más
energía consume de toda la casa (el valor máximo individual dentro de todas las
listas del diccionario), indicando en qué habitación se encuentra."""


def cargar_habitaciones():
    ambientes = {}

    for i in range(3):
        nombre_ambiente = input(f"Ingrese el nombre del ambiente {i+1}: ")
        aparatos = []

        while True:
            nombre_aparato = input("Ingrese el dispositivo activo: ")
            watts_consumidos = int(input("Ingrese su consumo en Watts: "))

            aparatos.append((nombre_aparato, watts_consumidos))

            seguir = input("¿Desea cargar otro dispositivo? (s/n): ")
            if seguir.lower() == "n":
                break

        ambientes[nombre_ambiente] = aparatos

    return ambientes


def mostrar_consumo(ambientes):
    print("Listado de habitaciones:")

    for ambiente, aparatos in ambientes.items():
        consumo_total = 0

        for aparato, watts in aparatos:
            consumo_total += watts

        print(f"Habitación: {ambiente} - Consumo: {consumo_total} Watts")


def buscar_mayor_consumo(ambientes):
    print("Dispositivo que más consume:")

    consumo_mayor = 0
    aparato_mayor = ""
    ambiente_mayor = ""

    for ambiente, aparatos in ambientes.items():
        for aparato, watts in aparatos:
            if watts > consumo_mayor:
                consumo_mayor = watts
                aparato_mayor = aparato
                ambiente_mayor = ambiente

    print(f"Dispositivo que más consume: {aparato_mayor}")
    print(f"Habitación: {ambiente_mayor}")
    print(f"Consumo: {consumo_mayor} Watts")


ambientes = cargar_habitaciones()
mostrar_consumo(ambientes)
buscar_mayor_consumo(ambientes)