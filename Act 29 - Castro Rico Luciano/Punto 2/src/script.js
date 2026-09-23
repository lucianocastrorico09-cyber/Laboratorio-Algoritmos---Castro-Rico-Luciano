/*Ejercicio 2: Carrito de Compras con Conteo de Productos
Enunciado: Crear un carrito de compras utilizando LocalStorage, que permita a los
usuarios agregar productos y muestre la cantidad total de productos en el carrito.
1. Los productos deben tener un botón para agregar al carrito.
2. Al agregar un producto, se debe mostrar el número total de productos en el
carrito, almacenándolo en LocalStorage.
3. Al recargar la página, el número total de productos debe recuperarse de
LocalStorage y mostrarse correctamente.*/


    document.addEventListener("DOMContentLoaded", function() {
      cargarCarrito();

      let botonesAgregar = document.getElementsByClassName("agregar-carrito");
      for (let i = 0; i < botonesAgregar.length; i++) {
        botonesAgregar[i].addEventListener("click", agregarProducto);
      }

      document.getElementById("vaciar-carrito").addEventListener("click", function() {
        localStorage.removeItem("carrito");
        cargarCarrito();
      });
    });

    function agregarProducto(event) {
      let producto = {
        id: event.target.getAttribute("data-id"),
        nombre: event.target.getAttribute("data-nombre"),
        precio: event.target.getAttribute("data-precio")
      };

      let carrito = JSON.parse(localStorage.getItem("carrito")) || [];
      carrito.push(producto);
      localStorage.setItem("carrito", JSON.stringify(carrito));

      cargarCarrito();
    }

    function cargarCarrito() {
      let listaCarrito = document.getElementById("lista-carrito");
      let totalProductos = document.getElementById("total-productos");
      listaCarrito.innerHTML = "";

      let carrito = JSON.parse(localStorage.getItem("carrito")) || [];

      totalProductos.textContent = carrito.length;

      for (let i = 0; i < carrito.length; i++) {
        let producto = carrito[i];
        let li = document.createElement("li");
        li.textContent = producto.nombre + " - $" + producto.precio;
        listaCarrito.appendChild(li);
      }
    }