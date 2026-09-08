/* 1. Crear un formulario con tres botones con las leyendas &quot;1&quot;, &quot;2&quot; y &quot;3&quot;.
Mostrar un mensaje indicando qué botón se presionó.*/

function mostrarBoton(numero){
    let mensaje = document.getElementById("mensaje")
    mensaje.textContent = "Se presiono el boton numero: " + numero
}