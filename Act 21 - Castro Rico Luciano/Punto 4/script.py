"""
4-
Se tiene que cargar los votos obtenidos por tres candidatos a una elección.
En una lista cargar en el primer componente el nombre del candidato y en la
segunda componente cargar una lista con componentes de tipo tupla con el
nombre de la provincia y la cantidad de votos obtenidos en dicha provincia.
Se deben cargar los datos por teclado.
1) Función para cargar todos los candidatos, sus nombres y las provincias con los
votos obtenidos.
2) Imprimir el nombre del candidato y la cantidad total de votos obtenidos en todas
las provincias.
"""
def carga():
    candidato=[]
    for i in range(3):
        nom=input(f"Ingrese el nombre del candidato {i+1}")
        tuplas=[]
        a=int(input(f"Cuantas provincias votaron a {nom}"))
        for x in range(a):
            vot=int(input(f"Ingrese la cantidad de votos que recibio el candidato {nom} en la provincia {x+1} "))
            tuplas.append(vot)
        tupla=tuple(tuplas)
        candidato.append([nom,tupla])
    return candidato

def imprimir(candidato):
    for i in range(3):
        suma=0
        for f in range(len(candidato[i][1])):
            suma=suma + candidato [i][1][f]
        print(f"El candidato {candidato[i][0]} recibio votos desde {len(candidato[i][1])} provincias y tiene un total de {suma} votos")
    



candidato = carga()
imprimir(candidato)