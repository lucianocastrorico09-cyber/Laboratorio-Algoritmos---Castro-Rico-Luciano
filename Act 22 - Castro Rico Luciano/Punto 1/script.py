"""1-
Crear un diccionario en Python que defina como clave el número de documento de
una persona y como valor un string con su nombre.
Desarrollar las siguientes funciones:
1) Cargar por teclado los datos de 4 personas.
2) Listado completo del diccionario.
3) Consulta del nombre de una persona ingresando su número de documento."""


def cargar_personas():
    personas = {}

    for i in range(4):
        dni = input("Ingrese DNI ")
        nombre = input("Ingrese nombre ")
        personas[dni] = nombre

    return personas


def listar_personas(personas):
    print("Listado completo")
    
    for dni in personas:
        print("DNI", dni, "- Nombre", personas[dni])


def consultar_persona(personas):
    dni = input("Ingrese DNI a consultar: ")

    if dni in personas:
        print("Nombre", personas[dni])
    else:
        print("No existe una persona con ese DNI")


personas = cargar_personas()
listar_personas(personas)
consultar_persona(personas)