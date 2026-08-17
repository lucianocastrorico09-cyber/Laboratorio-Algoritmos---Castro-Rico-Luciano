/*
Ejercicio 5: Gestión de Triaje en Guardia Médica (Prioridad)
Contexto: Un hospital atiende pacientes según la gravedad de su condición (Triaje), no
únicamente por orden de llegada. Los niveles de urgencia son: 1 (Normal), 2 (Moderado) y 3
(Crítico).
Consigna: La sala de espera se representa como una lista de registros sin diccionarios:
[[&quot;Paciente&quot;, Prioridad], ...]. Crear la función atender_siguiente(cola_espera) que seleccione
al próximo paciente en ser atendido.
Requisitos:
● Buscar al paciente que posea la prioridad más alta (mayor número).
● En caso de empate en la prioridad, se debe atender al primero que haya llegado a
la guardia (criterio FIFO).
● Eliminar al paciente seleccionado de la lista de espera y devolver un mensaje
indicando su nombre y nivel de urgencia.
Ejemplo de Entrada: [[&quot;Carlos&quot;, 1], [&quot;Ana&quot;, 3], [&quot;Roberto&quot;, 2], [&quot;Lucía&quot;, 3]] Salida
Esperada: Atiende primero a Ana (Nivel 3). Si se vuelve a llamar a la función,
la siguiente será Lucía (Nivel 3).*/

function atender_siguiente(cola_espera) {
  if (cola_espera.length === 0) {
    return "No hay pacientes en espera.";
  }

  let mayor = 0;

  for (let i = 1; i < cola_espera.length; i++) {
    if (cola_espera[i][1] > cola_espera[mayor][1]) {
      mayor = i;
    }
  }

  let paciente = cola_espera.splice(mayor, 1)[0];

  return "Atiende primero a " + paciente[0] + " (Nivel " + paciente[1] + ")";
}

let cola = [
  ["Carlos", 2],
  ["Ana", 1],
  ["Lucía", 3],
  ["Roberto", 3],
];

console.log(atender_siguiente(cola));
console.log(atender_siguiente(cola));

console.log("Pacientes restantes:");
console.log(cola);
