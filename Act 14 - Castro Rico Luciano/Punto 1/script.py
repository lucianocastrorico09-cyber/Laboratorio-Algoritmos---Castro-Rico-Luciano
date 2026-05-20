#1. Definir una lista que almacene por asignación los nombres de 5 personas.
#Contar cuántos de esos nombres tienen 5 o más caracteres y mostrarlo.

nombres = ["Luciano", "Fabian", "Benjamin", "Pablo", "Sebastian"]

contador = 0

for x in range (5):
    if len (nombres[x]) >= 5:
        contador += 1



print   (f"La cantidad de nombres con mas de 5 caracteres son {contador} ")