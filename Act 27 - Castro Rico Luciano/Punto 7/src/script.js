/*7. Confeccionar una página que muestre tres checkbox que permitan
seleccionar los deportes que practica el usuario (Fútbol, Básquet, Tenis)
Mostrar al presionar un botón los deportes que eligió.*/

function mostrar(){
    let basquet = document.getElementById("basquet").checked 
    let tenis = document.getElementById("tenis").checked
    let futbol = document.getElementById("futbol").checked
    let beisbol = document.getElementById("beisbol").checked

    let texto = "Deportes seleccionados: "

    if (basquet){
        texto = texto + "Basquet "
    }
    if (tenis){
        texto = texto + "Tenis "
    }
    if (futbol){
        texto = texto + "Futbol "
    }
    if (beisbol){
        texto = texto + "Beisbol "
    }

    if (!futbol && !basquet && !tenis && !beisbol){
        texto = "Usted no selecciono nada."
    }

    document.getElementById("deportes").textContent = texto
}