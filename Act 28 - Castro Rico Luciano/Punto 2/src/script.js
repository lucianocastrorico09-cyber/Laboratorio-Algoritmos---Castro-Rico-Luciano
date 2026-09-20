/*2. Confeccionar una página de visitas a un sitio, solicitar ingresar el nombre de una
persona, su mail y los comentarios (TEXTAREA). Mostrar luego llamando a la función
alert los datos ingresados.*/

function alerta() {
  let nombre = document.getElementById("nombre").value;
  let email = document.getElementById("email").value;
  let comentario = document.getElementById("comentarios").value;

  alert(
    "Datos ingresados " +
      "Nombre: " +
      nombre +
      "Email: " +
      email +
      "Comentario: " +
      comentario,
  );
}
