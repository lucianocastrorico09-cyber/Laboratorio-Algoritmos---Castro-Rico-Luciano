/*Ejercicio 03: Simulador de Votación en Línea
Plantear una página con 3 botones, cada uno representando un candidato distinto.
Al hacer clic en uno de los botones, se deberá aumentar el contador de votos de ese
candidato y mostrar el total actualizado en pantalla.
Además:
 El sistema debe mostrar en consola quién va ganando cada vez que se registra
un voto.
 Si hay un empate, debe mostrar el mensaje “Hay un empate”.*/

let votos1 = 0;
let votos2 = 0;
let votos3 = 0;

function votar(candidato) {
  if (candidato === 1) {
    votos1++;
  } else if (candidato === 2) {
    votos2++;
  } else if (candidato === 3) {
    votos3++;
  }

  document.getElementById("votos1").textContent = votos1;
  document.getElementById("votos2").textContent = votos2;
  document.getElementById("votos3").textContent = votos3;

  let mayor = Math.max(votos1, votos2, votos3);

  let cantidadGanadores = 0;

  if (votos1 === mayor) {
    cantidadGanadores++;
  }
  if (votos2 === mayor) {
    cantidadGanadores++;
  }
  if (votos3 === mayor) {
    cantidadGanadores++;
  }

  if (cantidadGanadores > 1) {
    console.log("Hay un empate");
  } else if (votos1 === mayor) {
    console.log("Va ganando Thiago Lopez");
  } else if (votos2 === mayor) {
    console.log("Va ganando Pablo Luque");
  } else {
    console.log("Va ganando Santino");
  }
}
