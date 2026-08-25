"""
3-
Un equipo de Fórmula 1 registra los nombres de sus 4 pilotos junto con los tiempos (en
segundos) obtenidos en sus últimas 3 vueltas de clasificación.
 La estructura de datos debe ser una lista general. Cada elemento de la lista será
una sublista que contenga en el primer componente el nombre del piloto (cadena
de caracteres) y en el segundo componente una tupla con sus 3 tiempos
(flotantes).
 Sugerencia de estructura interna si se cargara por asignación:
pilotos = [ ["Franco", (78.5, 77.2, 79.1)], ["Lewis", (77.9, 78.1, 77.4)], ... ]
Desarrollar las siguientes funciones:
1. Cargar pilotos: Solicitar por teclado el nombre de cada uno de los 4 pilotos y sus
3 mejores tiempos para estructurar la lista y las tuplas correspondientes.
2. Calcular Promedios: Recorrer la estructura de datos, calcular el tiempo promedio
de cada piloto en sus 3 vueltas e imprimir su nombre junto a dicho promedio.
3. Mejor Vuelta: Recorrer la estructura para buscar y mostrar la vuelta más rápida de
toda la clasificación (el tiempo individual más bajo dentro de cualquier tupla),
detallando a qué piloto le pertenece.
"""

def cargar_pilotos():
    pilotos = []

    for i in range(4):
        nombre = input(f"Ingrese el nombre del piloto N° {i + 1}: ")

        t1 = float(input("Ingrese el tiempo de la vuelta numero 1 (segundos): "))
        t2 = float(input("Ingrese el tiempo de la vuelta numero 2 (segundos): "))
        t3 = float(input("Ingrese el tiempo de la vuelta numero 3 (segundos): "))

        pilotos.append([nombre, (t1, t2, t3)])

    return pilotos


def promedios(pilotos):

    for piloto in pilotos:
        nombre = piloto[0]
        tiempos = piloto[1]

        promedio = sum(tiempos) / 3

        print(f"Piloto: {nombre}  Promedio: {promedio} segundos")


def mejor_vuelta(pilotos):
    mejor_tiempo = float("inf")
    mejor_piloto = ""

    for piloto in pilotos:
        nombre = piloto[0]
        tiempos = piloto[1]

        for tiempo in tiempos:
            if tiempo < mejor_tiempo:
                mejor_tiempo = tiempo
                mejor_piloto = nombre

    print(f"Piloto con mejor tiempo: {mejor_piloto}")
    print(f"Tiempo: {mejor_tiempo} segundos")


pilotos = cargar_pilotos()
promedios(pilotos)
mejor_vuelta(pilotos)
