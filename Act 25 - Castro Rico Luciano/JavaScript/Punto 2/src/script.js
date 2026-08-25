/*2-
Para un sistema de radares de tránsito, se necesita registrar la ubicación geográfica de 4
cámaras de control.
 Almacenar en una lista las coordenadas de las 4 cámaras. Cada elemento de la
lista debe ser una tupla de dos flotantes (latitud, longitud) ingresados por teclado.
Desarrollar las siguientes funciones:
1. Cargar coordenadas: Solicitar la latitud y la longitud de cada una de las 4
cámaras para armar las tuplas y agregarlas a la lista.
2. Listar posiciones: Recibir la lista e imprimir las coordenadas de todas las
cámaras. Importante: Realizar el recorrido utilizando un bucle for que
desempaquete la tupla directamente en las variables lat y lon en cada vuelta (sin
utilizar índices numéricos como [0] o [1]).
3. Filtrar hemisferio: Contar e informar cuántas de las cámaras se encuentran
ubicadas en el hemisferio norte (latitud mayor a cero).*/

function cargar() {
    let coordenadas = [];

    for (let i = 0; i < 4; i++) {
        console.log("Cámara " + (i + 1));

        let lat = parseFloat(prompt("Ingrese la latitud:"));
        let lon = parseFloat(prompt("Ingrese la longitud:"));

        coordenadas.push([lat, lon]);
    }

    return coordenadas;
}

function listarPosiciones(coordenadas) {
    console.log("Posiciones de las camaras:");

    for (let [lat, lon] of coordenadas) {
        console.log("Latitud:", lat, "Longitud:", lon);
    }
}

function filtrarHemisferio(coordenadas) {
    let cantidad = 0;

    for (let [lat, lon] of coordenadas) {
        if (lat > 0) {
            cantidad++;
        }
    }

    console.log(
        "Cantidad de camaras en el hemisferio norte:",
        cantidad
    );
}

let coordenadas = cargar();
listarPosiciones(coordenadas);
filtrarHemisferio(coordenadas);