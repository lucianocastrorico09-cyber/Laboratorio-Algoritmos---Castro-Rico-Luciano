/*4. Confeccionar una página que muestre un objeto SELECT con distintos
tipos de pizzas (Jamón y Queso, Muzzarella, Morrones). Al seleccionar
una, mostrar en un objeto de tipo TEXT el precio de la misma.*/

function seleccion(){
    let seleccionar = document.getElementById("select")
    let precio = seleccionar.value
    document.getElementById("texto").value = precio
} 