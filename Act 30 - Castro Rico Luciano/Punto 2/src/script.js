/*Ejercicio práctico #2:
Crear un carrito de compras dinámico con productos de una API
Enunciado: Vas a crear un carrito de compras dinámico que permite agregar
productos al carrito utilizando datos obtenidos de una API externa. Los pasos
específicos son:
1. Utilizá fetch() para obtener una lista de productos desde una API (puede ser la
misma API de productos del Ejercicio 1).
2. Mostrá los productos en la página en forma de tarjetas o lista.
3. Agregá un botón &quot;Añadir al carrito&quot; para cada producto. Al hacer clic en el
botón, el producto debe añadirse al carrito.
4. Usá LocalStorage para almacenar los productos que se agreguen al carrito,
de manera que si recarga la página, los productos sigan allí.
5. Mostrá la cantidad de productos que hay en el carrito en todo momento,
actualizándose cada vez que se añada un nuevo producto.*/

let API_URL = "https://fakestoreapi.com/products/category/electronics";

document.addEventListener("DOMContentLoaded", () => {
  obtenerProductosCarrito();
  cargarCarrito();

  let btnVaciar = document.getElementById("vaciar-carrito");
  if (btnVaciar) {
    btnVaciar.addEventListener("click", () => {
      localStorage.removeItem("carrito");
      cargarCarrito();
    });
  }
});

function obtenerProductosCarrito() {
  let contenedor = document.getElementById("productos-container");

  fetch(API_URL)
    .then((res) => {
      if (!res.ok) {
        throw new Error("No se pudo obtener la lista de productos");
      }
      return res.json();
    })
    .then((productos) => {
      mostrarProductos(productos);
    })
    .catch((error) => {
      console.error("Error al obtener productos:", error);
      if (contenedor) {
        contenedor.innerHTML =
          "<p>Error al cargar los productos del carrito.</p>";
      }
    });
}

function mostrarProductos(productos) {
  let contenedor = document.getElementById("productos-container");
  if (!contenedor) return;

  contenedor.innerHTML = "";

  productos.forEach((producto) => {
    let card = document.createElement("div");
    card.classList.add("card");
    card.innerHTML = `
      <img src="${producto.image}" alt="${producto.title}">
      <h3>${producto.title}</h3>
      <p>$${producto.price}</p>
      <button class="btn-agregar" 
        data-id="${producto.id}" 
        data-nombre="${producto.title.replace(/"/g, "&quot;")}" 
        data-precio="${producto.price}">
        Añadir al carrito
      </button>
    `;

    contenedor.appendChild(card);
  });

  let botones = document.querySelectorAll(".btn-agregar");
  botones.forEach((boton) => {
    boton.addEventListener("click", agregarProducto);
  });
}

function agregarProducto(e) {
  let producto = {
    id: e.target.getAttribute("data-id"),
    nombre: e.target.getAttribute("data-nombre"),
    precio: e.target.getAttribute("data-precio"),
  };

  let carrito = JSON.parse(localStorage.getItem("carrito")) || [];
  carrito.push(producto);
  localStorage.setItem("carrito", JSON.stringify(carrito));

  cargarCarrito();
}

function cargarCarrito() {
  let listaCarrito = document.getElementById("lista-carrito");
  let totalProductos = document.getElementById("total-productos");
  let carrito = JSON.parse(localStorage.getItem("carrito")) || [];

  if (totalProductos) {
    totalProductos.textContent = carrito.length;
  }

  if (listaCarrito) {
    listaCarrito.innerHTML = "";
    carrito.forEach((producto) => {
      let li = document.createElement("li");
      li.textContent = `${producto.nombre} - $${producto.precio}`;
      listaCarrito.appendChild(li);
    });
  }
}
