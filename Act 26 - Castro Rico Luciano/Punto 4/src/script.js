/*Ejercicio 04: Lista de Compras Dinámica

Confeccionar una página con un campo de texto y un botón “Agregar”.
Cada vez que se presione el botón, el producto ingresado en el campo debe añadirse
a una lista (&lt;ul&gt;).
Además:
 La lista debe permitir eliminar un producto haciendo clic sobre él.
 En consola debe mostrarse en todo momento la cantidad de productos
actuales en la lista.*/

function agregarProducto() {
  let input = document.getElementById("producto");
  let texto = input.value;

  if (texto === "") {
    return;
  }

  let lista = document.getElementById("lista");
  let nuevoItem = document.createElement("li");
  nuevoItem.textContent = texto;

  nuevoItem.onclick = function () {
    lista.removeChild(nuevoItem);
    mostrarCantidad();
  };

  lista.appendChild(nuevoItem);
  input.value = "";

  mostrarCantidad();
}

function mostrarCantidad() {
  let lista = document.getElementById("lista");
  let cantidad = lista.children.length;
  console.log("Cantidad de productos en la lista: " + cantidad);
}
