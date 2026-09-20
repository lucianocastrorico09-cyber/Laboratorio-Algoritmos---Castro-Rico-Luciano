/* 1. Confeccionar una página que muestre dos objetos de la clase RADIO solicitando que
seleccione si es mayor de 18 años o no. Al presionar un botón mostrar un alert
indicando si puede ingresar al sitio o no.*/

function boton() {
  let radio1 = document.getElementById("radio1").checked;
  let radio2 = document.getElementById("radio2").checked;

  if (radio1) {
    alert("Es mayor de edad");
  }
  if (radio2) {
    alert("Es menor de edad");
  }
}
