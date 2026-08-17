/*
Ejercicio 3: Tabla de Posiciones con Desempate (Listas Paralelas)
Contexto: Se está organizando un torneo deportivo y se necesita generar la tabla de
posiciones a partir de tres listas paralelas sincronizadas por índice: equipos, puntos y
diferencia_gol.
Consigna: Diseñar un algoritmo de ordenamiento que reorganice las tres listas de mayor a
menor según el desempeño de cada equipo.
Requisitos:
● Criterio Principal: Mayor cantidad de puntos.
● Criterio de Desempate: Si dos o más equipos empatan en puntos, la posición se
define por el equipo que tenga la mayor diferencia de gol.
● Mantener la sincronización perfecta entre las tres listas al realizar los intercambios.
Ejemplo de Entrada: equipos = [&quot;Boca&quot;, &quot;River&quot;, &quot;Racing&quot;] puntos = [12, 15, 12]
diferencia_gol = [8, 5, 10] Salida Esperada: 1° River (15 pts), 2° Racing (12 pts,
DG 10), 3° Boca (12 pts, DG 8).
 */

function ordenar_tabla(equipos, puntos, diferencia_gol) {
  let n = equipos.length;

  for (let i = 0; i < n - 1; i++) {
    for (let j = 0; j < n - 1 - i; j++) {
      let cambiar = false;

      if (puntos[j] < puntos[j + 1]) {
        cambiar = true;
      } else if (puntos[j] === puntos[j + 1]) {
        if (diferencia_gol[j] < diferencia_gol[j + 1]) {
          cambiar = true;
        }
      }

      if (cambiar) {
        let aux = equipos[j];
        equipos[j] = equipos[j + 1];
        equipos[j + 1] = aux;

        aux = puntos[j];
        puntos[j] = puntos[j + 1];
        puntos[j + 1] = aux;

        aux = diferencia_gol[j];
        diferencia_gol[j] = diferencia_gol[j + 1];
        diferencia_gol[j + 1] = aux;
      }
    }
  }
}

let equipos = ["Boca", "River", "Racing"];
let puntos = [12, 15, 12];
let diferencia_gol = [8, 5, 10];

ordenar_tabla(equipos, puntos, diferencia_gol);

console.log("Tabla de posiciones:");

for (let i = 0; i < equipos.length; i++) {
  console.log(
    `${i + 1}° ${equipos[i]} - ${puntos[i]} pts - DG ${diferencia_gol[i]}`,
  );
}
