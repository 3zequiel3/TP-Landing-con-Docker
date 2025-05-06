console.log("✅ script.js ha sido cargado");

/**Parte 4*/
/*Seleccion de Datos por producto */
/*Esta linea de codigo se encarga de hacer que cada vez que se aprieta un boton de comprar se
* redirija directamente a una plantilla, y rellene esa plantilla en funcion de los datos del producto a comprar*/
/***************/
/*Galeria - parte 3 - Hice cambios aca, a partir de la linea 12 a la 33.*/
console.log("✅ script.js ha sido cargado correctamente");

// 📌 Asignar eventos usando DOM a los botones "Comprar"
document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".comprar-btn").forEach(button => {
        button.addEventListener("click", function () {
            let item = this.closest(".carousel-item, .card");

            if (!item) {
                console.error("❌ No se encontró el producto.");
                return;
            }

            let name = item.querySelector("h3, .card-title")?.textContent.trim() || "Producto sin nombre";
            let desc = item.querySelector("p, .card-text")?.textContent.trim() || "Sin descripción disponible";
            let img = item.querySelector("img")?.src || "img/default.png";
            let price = item.querySelector(".precio")?.textContent.trim() || "Precio no disponible";

            console.log("📤 Enviando datos:", { name, desc, img, price });

            let url = `producto.html?name=${encodeURIComponent(name)}&desc=${encodeURIComponent(desc)}&img=${encodeURIComponent(img)}&price=${encodeURIComponent(price)}`;
            window.location.href = url;
        });
    });
});

    // 📌 Cargar los datos en producto.html
    if (document.getElementById("producto-nombre")) {
        const params = new URLSearchParams(window.location.search);

        let nombre = params.get("name");
        let imagen = params.get("img");
        let descripcion = params.get("desc");

        console.log("🔍 Datos recibidos desde la URL:", { nombre, imagen, descripcion });

        if (nombre && imagen && descripcion) {
            document.getElementById("producto-nombre").textContent = nombre;
            document.getElementById("producto-imagen").src = imagen;
            document.getElementById("producto-imagen").alt = `Imagen de ${nombre}`;
            document.getElementById("producto-descripcion").textContent = descripcion;
        } else {
            console.error("❌ No se encontraron datos en la URL.");
        }
    }
/***************/
