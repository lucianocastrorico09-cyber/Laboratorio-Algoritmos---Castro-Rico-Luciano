/*Ejercicio práctico #1:
Aplicar el consumo de API Fetch en tu proyecto personal
Enunciado: En este ejercicio, vas a integrar el consumo de una API REST utilizando
fetch() en tu proyecto personal de e-commerce o cualquier otro proyecto que estés
desarrollando. Los pasos a seguir son:
1. Elige una API pública (como Fake Store API) que te proporcione datos de
productos, usuarios y usuarias o cualquier otro recurso que quieras mostrar en
tu proyecto.
2. Usa fetch() para hacer una solicitud a la API y obtener los datos.
3. Muestra los datos obtenidos en tu proyecto, ya sea en forma de lista de
productos, usuarias o usuarios o lo que elijas.
4. Asegúrate de manejar los posibles errores utilizando .catch() y mostrá un
mensaje si algo falla.
5. Opcional: Integra los datos obtenidos con alguna funcionalidad de tu proyecto,
como un carrito de compras o una lista de productos favoritos.*/

const API_URL = "https://fakestoreapi.com/products/category/electronics";

document.addEventListener("DOMContentLoaded", () => {
  actualizarContadorFavoritos();
  obtenerProductos();
});

function obtenerProductos() {
  const contenedor = document.getElementById("product-container");
  const loading = document.getElementById("loading");

  fetch(API_URL)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Error en la respuesta de la red");
      }
      return response.json();
    })
    .then((productos) => {
      if (loading) loading.style.display = "none";
      if (!contenedor) return;

      let cardsHTML = "";

      productos.forEach((producto) => {
        cardsHTML += `
          <div class="card">
            <img src="${producto.image}" alt="${producto.title}">
            <h2>${producto.title}</h2>
            <h3>$${producto.price}</h3>
            <p>Categoría: ${producto.category}</p>
            <button onclick="agregarFavorito(${producto.id})">Añadir a favoritos</button>
          </div>
        `;
      });

      contenedor.innerHTML = cardsHTML;
    })
    .catch((error) => {
      console.error("Error al obtener productos:", error);
      if (loading) loading.style.display = "none";
      if (contenedor) {
        contenedor.innerHTML =
          "<p class='error-msg'>Ocurrió un error al cargar los datos. Por favor, intenta de nuevo.</p>";
      }
    });
}

function agregarFavorito(idProducto) {
  let favoritos = JSON.parse(localStorage.getItem("favoritos")) || [];

  if (!favoritos.includes(idProducto)) {
    favoritos.push(idProducto);
    localStorage.setItem("favoritos", JSON.stringify(favoritos));

    actualizarContadorFavoritos();
    alert("¡Producto añadido a favoritos!");
  } else {
    alert("Este producto ya está en tus favoritos.");
  }
}

function actualizarContadorFavoritos() {
  const favoritos = JSON.parse(localStorage.getItem("favoritos")) || [];
  const contador = document.getElementById("cant-favoritos");

  if (contador) {
    contador.textContent = favoritos.length;
  }
}
