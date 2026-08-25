/*4-
Un comercio de tecnología necesita administrar el stock de sus 5 componentes clave de
hardware.
 Crear una lista donde cada elemento sea una tupla de tres elementos que
represente: (nombre_articulo, precio, stock).
Desarrollar las siguientes funciones:
1. Cargar inventario: Ingresar por teclado los datos de los 5 componentes para
armar las tuplas correspondientes.
2. Imprimir listado: Mostrar por pantalla los nombres, precios y stock de todos los
artículos desempaquetando la tupla de manera directa en el bucle for.
3. Valor del Inventario: Calcular e informar el valor total de la mercadería en el local
(sumando el resultado de precio * stock de cada uno de los componentes).
4. Alerta de Reposición: Imprimir el nombre de todos aquellos artículos cuyo stock
*/

function cargar() {
    let inventario = [];

    for (let i = 0; i < 5; i++) {
        console.log("Componente", i + 1);

        let nombre = prompt("Ingrese el nombre del articulo:");
        let precio = parseFloat(prompt("Ingrese el precio:"));
        let stock = parseInt(prompt("Ingrese el stock:"));

        let articulo = {
            nombre: nombre,
            precio: precio,
            stock: stock
        };

        inventario.push(articulo);
    }

    return inventario;
}

function imprimirListado(inventario) {
    console.log("Listado de articulos:");

    for (let articulo of inventario) {
        console.log("Articulo:", articulo.nombre);
        console.log("Precio:", articulo.precio);
        console.log("Stock:", articulo.stock);
    }
}

function valorInventario(inventario) {
    let total = 0;

    for (let articulo of inventario) {
        total += articulo.precio * articulo.stock;
    }

    console.log("Valor total del inventario:", total);
}

function alertaReposicion(inventario) {
    console.log("Artículos que necesitan reposicion:");

    for (let articulo of inventario) {
        if (articulo.stock <= 10) {
            console.log("Comprar urgentemente:", articulo.nombre);
        }
    }
}

let inventario = cargar();

imprimirListado(inventario);
valorInventario(inventario);
alertaReposicion(inventario);