/*3. Disponer dos campos de texto tipo password. Cuando se presione un
botón mostrar si las dos claves ingresadas son iguales o no (es muy
común solicitar al operador el ingreso de dos veces de su clave para
validar si las escribió correctamente, esto se hace cuando se crea una
password para el ingreso a un sitio o para el cambio de una existente).
Tener en cuenta que podemos emplear el operador == para ver si dos
string son iguales.*/

function verificar(){
    let contra1 = document.getElementById("contra1").value
    let contra2 = document.getElementById("contra2").value
    let mensaje = document.getElementById("mensaje")

    if (contra1 == contra2){
        mensaje.textContent = "Las contraseñas son iguales."
        mensaje.style.color = "green"
    }
    else {
        mensaje.textContent = "Las contraseñas son distintas, revise las dos mencionadas."
        mensaje.style.color = "red"
    }
}