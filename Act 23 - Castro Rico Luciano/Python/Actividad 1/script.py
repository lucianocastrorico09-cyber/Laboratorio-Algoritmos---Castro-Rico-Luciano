"""
Ejercicio 1: Sistema de Reserva de Butacas (Matrices 2D)
Contexto: Un cine necesita un módulo automatizado para vender entradas. La sala se
representa como una matriz (lista de listas) de N filas por M columnas, donde un 0
representa un asiento libre y un 1 uno ocupado.
Consigna:
Escribir una función llamada reservar_consecutivos(sala, fila, cantidad) que reciba la matriz
de la sala, el número de fila deseado y la cantidad de entradas que desea comprar el grupo
de clientes.
Requisitos:
● Debe buscar si existen suficientes asientos libres y contiguos (juntos) en esa
misma fila.
● Si los encuentra, debe cambiar sus valores a 1 (ocupados) y retornar un mensaje
confirmando la reserva con los números de columna asignados.
● Si no hay espacio consecutivo suficiente, debe indicar que no fue posible realizar la
reserva sin modificar la sala.
Ejemplo de Entrada:
Sala de 3x5. En la fila 0, la columna 1 ya está ocupada: [ [0, 1, 0, 0, 0], ... ]
Intentar reservar 3 asientos en la fila 0.
Salida Esperada: Confirmación de reserva para las columnas 2, 3 y 4.
"""

def reservar_consecutivos(sala, fila, cantidad):
    columnas = len(sala[fila])

    for inicio in range(columnas - cantidad + 1):
        libres = True

        for j in range(inicio, inicio + cantidad):
            if sala[fila][j] == 1:
                libres = False
                break

        if libres:
            reservadas = []
            for j in range(inicio, inicio + cantidad):
                sala[fila][j] = 1
                reservadas.append(j)

            return f"Reserva confirmada. Columnas: {reservadas}"

    return "No fue posible realizar la reserva."



sala = [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

print(reservar_consecutivos(sala, 2, 2))
print(sala)
