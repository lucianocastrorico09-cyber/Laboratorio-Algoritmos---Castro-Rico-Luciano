"""
Un observatorio astronómico registra los descubrimientos de nuevos planetas
fuera del sistema solar.
 Diseñar un diccionario donde la Clave sea el nombre científico del
exoplaneta (ej: &quot;Kepler-22b&quot;) y el Valor sea una tupla con sus datos:
(distancia_anios_luz, tipo_de_atmosfera, es_habitable_booleano).
Desarrollar las siguientes funciones:
1. Cargar catálogo: Registrar por teclado la información de 4 exoplanetas
descubiertos.
2. Buscar exoplaneta: Permitir al usuario ingresar el nombre de un
exoplaneta por teclado. Si el exoplaneta se encuentra en el diccionario
(utilizando el operador in), mostrar todos sus detalles físicos y si reúne
condiciones de habitabilidad. De lo contrario, mostrar un cartel indicando:
&quot;El exoplaneta no figura en el catálogo actual&quot;.
3. Reportar Habitables: Mostrar en pantalla únicamente los nombres de los
exoplanetas cargados que fueron marcados como habitables.
"""
def cargar_catalogo():
    planetas = {}

    for i in range(4):
        nombre = input("Nombre del exoplaneta ")
        distancia = float(input("Distancia en años luz "))
        atmosfera = input("Tipo de atmósfera ")
        habitable = input("Es habitable? (si/no) ")

        if habitable == "si":
            habitable = True
        else:
            habitable = False

        planetas[nombre] = (distancia, atmosfera, habitable)

    return planetas


def buscar_exoplaneta(planetas):
    nombre = input("Ingrese nombre del exoplaneta ")

    if nombre in planetas:
        distancia, atmosfera, habitable = planetas[nombre]

        print("Distancia:", distancia)
        print("Atmósfera:", atmosfera)
        print("Habitable:", habitable)
    else:
        print("El exoplaneta no figura en el catálogo actual")


def reportar_habitables(planetas):
    print("Exoplanetas habitables:")

    for nombre in planetas:
        distancia, atmosfera, habitable = planetas[nombre]

        if habitable == True:
            print(nombre)


planetas = cargar_catalogo()
buscar_exoplaneta(planetas)
reportar_habitables(planetas)