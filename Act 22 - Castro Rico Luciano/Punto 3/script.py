"""3
Un equipo de seguridad informática registra las direcciones IP de servidores
sospechosos que intentan acceder de forma no autorizada al sistema.
 Crear un diccionario donde la Clave sea la dirección IP (cadena de
caracteres, ej: &quot;192.168.1.50&quot;) y el Valor sea una tupla que contenga:
(nombre_del_dispositivo, cantidad_intentos_fallidos).
Desarrollar las siguientes funciones:
1. Cargar registro: Solicitar por teclado la carga de 4 direcciones IP
sospechosas junto a los datos del dispositivo y sus intentos fallidos.
2. Listar amenazas: Imprimir la lista de todas las IPs registradas indicando
qué dispositivo es y cuántos intentos realizó.
3. Filtrar Bloqueos: Recorrer el diccionario e informar las direcciones IP que
deben ser bloqueadas inmediatamente por seguridad (aquellas con más de
5 intentos fallidos).
"""
def cargar_registro():
    amenazas = {}

    for i in range(4):
        ip = input("Ingrese IP ")
        dispositivo = input("Nombre del dispositivo ")
        intentos = int(input("Intentos fallidos "))

        amenazas[ip] = (dispositivo, intentos)

    return amenazas


def listar_amenazas(amenazas):
    print("Lista de amenazas")

    for ip in amenazas:
        dispositivo, intentos = amenazas[ip]
        print("IP", ip)
        print("Dispositivo", dispositivo)
        print("Cantidad de intentos", intentos)


def filtrar_bloqueos(amenazas):
    print("IPs a bloquear")

    for ip in amenazas:
        dispositivo, intentos = amenazas[ip]

        if intentos > 5:
            print(ip)


amenazas = cargar_registro()
listar_amenazas(amenazas)
filtrar_bloqueos(amenazas)