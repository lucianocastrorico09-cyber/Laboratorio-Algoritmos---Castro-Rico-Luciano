"""1-
Una ciudad inteligente cuenta con sensores que miden las partículas contaminantes de
dióxido de carbono (CO2) en diferentes puntos geográficos.
 Crear un diccionario donde la Clave sea el nombre del barrio o estación de
monitoreo (ej: &quot;San Telmo&quot;) y el Valor sea una lista de flotantes que represente
las últimas 3 lecturas de contaminación tomadas en el día.
Desarrollar las siguientes funciones:
1. Cargar sensores: Ingresar por teclado 3 estaciones de monitoreo y, para cada
una, solicitar las 3 lecturas consecutivas de CO2 (en partes por millón - ppm).
2. Reportar promedios: Calcular y mostrar el promedio de contaminación de cada
barrio.
3. Alerta ambiental: Mostrar en pantalla una alerta roja de &quot;Protocolo de
Emergencia&quot; únicamente para las estaciones cuyo promedio de contaminación
supere las 400 ppm."""

datos_co2 = {}

def cargar_datos():
    for i in range(3):
        barrio = input("Ingrese el nombre del barrio: ")
        mediciones = []

        for j in range(3):
            co2 = float(input("Ingrese la medición de CO2 (ppm): "))
            mediciones.append(co2)

        datos_co2[barrio] = mediciones


def mostrar_promedios():
    print("Promedios de contaminación")

    for barrio, mediciones in datos_co2.items():
        promedio = sum(mediciones) / 3

        print(barrio, ":", promedio, "ppm")


def mostrar_alertas():
    print("Alertas ambientales")

    for barrio, mediciones in datos_co2.items():
        promedio = sum(mediciones) / 3

        if promedio > 400:
            print("Protocolo de Emergencia")
            print("Barrio:", barrio)
            print("Promedio:", promedio, "ppm")


cargar_datos()
mostrar_promedios()
mostrar_alertas()