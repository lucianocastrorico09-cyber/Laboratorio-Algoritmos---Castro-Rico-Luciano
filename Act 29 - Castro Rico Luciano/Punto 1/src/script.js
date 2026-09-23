/*Ejercicio 1: Guardar Preferencias de Usuario
Enunciado: Crear una función que guarde y recupere las preferencias de un usuario,
como su nombre y el color de fondo preferido, utilizando LocalStorage.
1. La función debe permitir al usuario ingresar su nombre y seleccionar su color
de fondo preferido desde una lista de opciones.
2. Los datos ingresados deben almacenarse en LocalStorage.
3. Cada vez que la página se recargue, las preferencias deben recuperarse de
LocalStorage y aplicarse automáticamente (mostrar el nombre del usuario y
cambiar el color de fondo).*/

    document.addEventListener("DOMContentLoaded", function() {
      cargarPreferencias();

      document.getElementById("botonGuardar").addEventListener("click", guardarPreferencias);
    });

    function guardarPreferencias() {
      let nombre = document.getElementById("nombre").value;
      let color = document.getElementById("colorFondo").value;

      localStorage.setItem("nombreUsuario", nombre);
      localStorage.setItem("colorFondo", color); 

      cargarPreferencias();
    }


    function cargarPreferencias() {
      let nombre = localStorage.getItem("nombreUsuario") || "";
      let color = localStorage.getItem("colorFondo") || "#ffffff";

      document.body.style.backgroundColor = color;
      
      let saludo = document.getElementById("saludo");
      if (nombre) {
        saludo.textContent = "¡Hola, " + nombre + "!";
      } else {
        saludo.textContent = "";
      }
    }