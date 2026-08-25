/* 1-
Confeccionar un programa que permita registrar las temperaturas máximas de las últimas
6 horas en una lista.
Desarrollar las siguientes funciones:
1. Carga: Solicitar al operador el ingreso por teclado de las 6 temperaturas y
almacenarlas en una lista.
2. Procesar Extremos: Recibir la lista como parámetro y retornar una tupla que
contenga en su primer componente el valor máximo y en el segundo el valor
mínimo.
3. Bloque Principal: Desempaquetar la tupla devuelta por la función anterior en dos
variables individuales (máxima y mínima) y mostrarlas en pantalla con un mensaje
descriptivo.*/

function cargar() {
    let temperaturas = [];

    for (let i = 0; i < 6; i++) {
        let temperatura = parseInt(
            prompt("Ingrese la temperatura" + (i + 1))
        );

        temperaturas.push(temperatura);
    }

    return temperaturas;
}

function extremos(temperaturas) {
    let maximo = temperaturas[0];
    let minimo = temperaturas[1];

    for (let temperatura of temperaturas) {
        if (maximo < temperatura) {
            maximo = temperatura;
        } else if (minimo > temperatura) {
            minimo = temperatura;
        }
    }

    return [maximo, minimo];
}

let temperaturas = cargar();

let [maximo, minimo] = extremos(temperaturas);

console.log("La temperatura máxima es:" + {maximo});
console.log("La temperatura mínima es:" + {minimo});