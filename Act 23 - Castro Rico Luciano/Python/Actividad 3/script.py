

"""Ejercicio 3: Tabla de Posiciones con Desempate (Listas Paralelas)
Contexto: Se está organizando un torneo deportivo y se necesita generar la tabla de
posiciones a partir de tres listas paralelas sincronizadas por índice: equipos, puntos y
diferencia_gol.
Consigna: Diseñar un algoritmo de ordenamiento que reorganice las tres listas de mayor a
menor según el desempeño de cada equipo.
Requisitos:
● Criterio Principal: Mayor cantidad de puntos.
● Criterio de Desempate: Si dos o más equipos empatan en puntos, la posición se
define por el equipo que tenga la mayor diferencia de gol.
● Mantener la sincronización perfecta entre las tres listas al realizar los intercambios.
Ejemplo de Entrada: equipos = [&quot;Boca&quot;, &quot;River&quot;, &quot;Racing&quot;] puntos = [12, 15, 12]
diferencia_gol = [8, 5, 10] Salida Esperada: 1° River (15 pts), 2° Racing (12 pts,
DG 10), 3° Boca (12 pts, DG 8)."""


def ordenar_tabla(equipos, puntos, diferencia_gol):
    n = len(equipos)

    for i in range(n - 1):
        for j in range(n - 1 - i):

            if puntos[j] < puntos[j + 1]:

                equipos[j], equipos[j + 1] = equipos[j + 1], equipos[j]
                puntos[j], puntos[j + 1] = puntos[j + 1], puntos[j]
                diferencia_gol[j], diferencia_gol[j + 1] = diferencia_gol[j + 1], diferencia_gol[j]

            elif puntos[j] == puntos[j + 1]:

                if diferencia_gol[j] < diferencia_gol[j + 1]:

                    equipos[j], equipos[j + 1] = equipos[j + 1], equipos[j]
                    puntos[j], puntos[j + 1] = puntos[j + 1], puntos[j]
                    diferencia_gol[j], diferencia_gol[j + 1] = diferencia_gol[j + 1], diferencia_gol[j]


equipos = ["Boca", "River", "Racing"]
puntos = [12, 15, 12]
diferencia_gol = [8, 5, 10]

ordenar_tabla(equipos, puntos, diferencia_gol)

print("Tabla de posiciones:")

for i in range(len(equipos)):
    print(f"{i + 1}° {equipos[i]} - {puntos[i]} pts - DG {diferencia_gol[i]}")