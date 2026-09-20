/*3. Solicitar que se ingrese el nombre y la clave de un usuario. Mostrar una ventana de
alerta si en la clave se ingresan menos de 7 caracteres o más de 20 (capturar el evento
onBlur)*/

function verificarClave() {
  let contra = document.getElementById("contra").value;

  if (contra.length < 7 || contra.length > 20) {
    alert("La contraseña debe tener entre 7 y 20 caracteres");
  }
}
