/*3-
Un equipo de Fórmula 1 registra los nombres de sus 4 pilotos junto con los tiempos (en
segundos) obtenidos en sus últimas 3 vueltas de clasificación.
 La estructura de datos debe ser una lista general. Cada elemento de la lista será
una sublista que contenga en el primer componente el nombre del piloto (cadena
de caracteres) y en el segundo componente una tupla con sus 3 tiempos
(flotantes).
 Sugerencia de estructura interna si se cargara por asignación:
pilotos = [ ["Franco", (78.5, 77.2, 79.1)], ["Lewis", (77.9, 78.1, 77.4)], ... ]
Desarrollar las siguientes funciones:
1. Cargar pilotos: Solicitar por teclado el nombre de cada uno de los 4 pilotos y sus
3 mejores tiempos para estructurar la lista y las tuplas correspondientes.
2. Calcular Promedios: Recorrer la estructura de datos, calcular el tiempo promedio
de cada piloto en sus 3 vueltas e imprimir su nombre junto a dicho promedio.
3. Mejor Vuelta: Recorrer la estructura para buscar y mostrar la vuelta más rápida de
toda la clasificación (el tiempo individual más bajo dentro de cualquier tupla),
detallando a qué piloto le pertenece */

function cargar() {
    let pilotos = [];

    for (let i = 0; i < 4; i++) {
        let nombre = prompt(`Ingrese el nombre del piloto ${i + 1}:`);

        let tiempo1 = parseFloat(prompt("Ingrese el tiempo de la vuelta 1:"));
        let tiempo2 = parseFloat(prompt("Ingrese el tiempo de la vuelta 2:"));
        let tiempo3 = parseFloat(prompt("Ingrese el tiempo de la vuelta 3:"));

        let tiempos = [tiempo1, tiempo2, tiempo3];

        pilotos.push([nombre, tiempos]);
    }

    return pilotos;
}


function calcularPromedios(pilotos) {
    console.log("Promedios:");

    for (let [nombre, tiempos] of pilotos) {
        let suma = 0;

        for (let tiempo of tiempos) {
            suma += tiempo;
        }

        let promedio = suma / 3;

        console.log(nombre, " ", promedio, "segundos");
    }
}


function mejorVuelta(pilotos) {
    let mejorTiempo = Infinity;
    let mejorPiloto = "";

    for (let [nombre, tiempos] of pilotos) {
        for (let tiempo of tiempos) {
            if (tiempo < mejorTiempo) {
                mejorTiempo = tiempo;
                mejorPiloto = nombre;
            }
        }
    }

    console.log("Mejor vuelta:");
    console.log("Piloto:", mejorPiloto);
    console.log("Tiempo:", mejorTiempo, "segundos");
}


let pilotos = cargar();

calcularPromedios(pilotos);
mejorVuelta(pilotos);