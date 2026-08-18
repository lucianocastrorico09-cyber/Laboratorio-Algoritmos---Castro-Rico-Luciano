"""2-
En un videojuego multijugador en línea, los jugadores se agrupan en clanes o gremios
para realizar misiones cooperativas.
 Diseñar un diccionario donde la Clave sea el nombre del Gremio (ej:
&quot;DragonesDeFuego&quot;) y el Valor sea una lista de cadenas con los nombres de
los jugadores (nicknames) que lo integran.
Desarrollar las siguientes funciones:
1. Registrar gremios: Cargar por teclado 3 gremios. Para cada gremio, se debe
preguntar cuántos integrantes posee para cargar sus respectivos nombres de
usuario en la lista interna.
2. Listar clanes: Mostrar los nombres de todos los gremios junto a la cantidad total
de miembros que posee cada uno.
3. Buscar jugador: Solicitar por teclado el nombre de un jugador y buscar en qué
gremio está registrado. Informar el gremio encontrado o indicar si el jugador es
&quot;Solitario&quot; (no pertenece a ningún clan)."""


def cargar_clanes():
    clanes = {}

    for i in range(3):
        nombre_clan = input(f"Ingrese el nombre del clan {i + 1}: ")
        total_miembros = int(input(f"¿Cuántos integrantes tiene {nombre_clan}? "))
        miembros = []

        for j in range(total_miembros):
            nickname = input(f"Ingrese el nombre del jugador {j + 1}: ")
            miembros.append(nickname)

        clanes[nombre_clan] = miembros

    return clanes


def mostrar_clanes(clanes):
    print("Lista de clanes: ")

    for clan, miembros in clanes.items():
        print(f"Clan: {clan} - Cantidad de miembros: {len(miembros)}")


def encontrar_jugador(clanes):
    nombre_buscar = input("Ingrese el nombre del jugador a buscar: ")

    esta_encontrado = False

    for clan, miembros in clanes.items():
        if nombre_buscar in miembros:
            print(f"El jugador {nombre_buscar} pertenece al clan: {clan}")
            esta_encontrado = True
            break

    if not esta_encontrado:
        print(f"El jugador {nombre_buscar} es Solitario.")


clanes = cargar_clanes()
mostrar_clanes(clanes)
encontrar_jugador(clanes)