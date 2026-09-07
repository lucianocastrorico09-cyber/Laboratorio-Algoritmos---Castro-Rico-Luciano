/*Ejercicio 05: Control de Temperatura
Diseñar una página con un campo de texto para ingresar una temperatura y un botón
“Verificar”.
Cuando el usuario haga clic:
 Si la temperatura es menor a 10, mostrar en el documento el mensaje “Hace
frío” en azul.
 Si está entre 10 y 25, mostrar “Clima agradable” en verde.
 Si es mayor a 25, mostrar “Hace calor” en rojo.
Además, cada verificación debe registrarse en consola con la fecha y hora
exacta (usando Date()).*/

function verificarTemperatura() {
  let temperatura = Number(document.getElementById("temperatura").value);
  let resultado = document.getElementById("resultado");

  if (temperatura < 10) {
    resultado.textContent = "Hace frio";
    resultado.style.color = "blue";
  } else if (temperatura > 10 && temperatura <= 25) {
    resultado.textContent = "Clima agradable";
    resultado.style.color = "green";
  } else if (temperatura > 25) {
    resultado.textContent = "Hace calor";
    resultado.style.color = "red";
  }

  console.log("Se hizo la verificacion. " + new Date());
}
