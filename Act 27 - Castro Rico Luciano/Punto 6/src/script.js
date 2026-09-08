/*6. Confeccionar una página que permita tomar un examen múltiple choice.
Se debe mostrar una pregunta y seguidamente un objeto SELECT con
las respuestas posibles. Al presionar un botón mostrar la cantidad de
respuestas correctas e incorrectas (Disponer 4 preguntas y sus
respectivos controles SELECT)*/

function corregir(){
    let correctas = 0;
    let incorrectas = 0;

    let respuesta1 = document.getElementById("pregunta1").value;
    let respuesta2 = document.getElementById("pregunta2").value;
    let respuesta3 = document.getElementById("pregunta3").value;
    let respuesta4 = document.getElementById("pregunta4").value;

    if (respuesta1 == "Buenos Aires"){
        correctas++;
    }
    else {
        incorrectas++;
    }

    if (respuesta2 == "4"){
        correctas++;
    }
    else {
        incorrectas++;
    }
    if (respuesta3 == "JavaScript"){
        correctas++;
    }
    else {
        incorrectas++;
    }
    if (respuesta4 == "Micky Mouse"){
        correctas++;
    }
    else {
        incorrectas++;
    }
    
    let resultado = document.getElementById("resultado")
    resultado.textContent = "Correctas: " + correctas + " - Incorrectas: " + incorrectas;
}