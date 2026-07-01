"""2-
Se desea almacenar los datos de 3 alumnos. Definir un diccionario cuya clave sea
el número de documento del alumno. Como valor almacenar una lista con
componentes de tipo tupla donde almacenamos nombre de materia y su nota.
Crear las siguientes funciones:
1) Carga de los alumnos (de cada alumno solicitar su dni y los nombres de las
materias y sus notas)
2) Listado de todos los alumnos con sus notas
3) Consulta de un alumno por su dni, mostrar las materias que cursa y sus notas."""



def cargar_alumnos():
    alumnos = {}

    for i in range(3):
        dni = input("Ingrese DNI del alumno ")
        materias = []

        cantidad = int(input("Cantidad de materias "))

        for j in range(cantidad):
            materia = input("Nombre de materia ")
            nota = int(input("Nota "))
            materias.append((materia, nota))

        alumnos[dni] = materias

    return alumnos


def listar_alumnos(alumnos):
    print("Listado de alumnos")

    for dni in alumnos:
        print("DNI", dni)

        for materia, nota in alumnos[dni]:
            print("Materia", materia, "- Nota", nota)


def consultar_alumno(alumnos):
    dni = input("Ingrese DNI a consultar ")

    if dni in alumnos:
        for materia, nota in alumnos[dni]:
            print("Materia", materia, "- Nota", nota)
    else:
        print("Alumno no encontrado")


alumnos = cargar_alumnos()
listar_alumnos(alumnos)
consultar_alumno(alumnos)
