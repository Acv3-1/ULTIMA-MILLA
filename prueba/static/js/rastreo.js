function initMap(lat = 4.813671, lng = -74.354530) {
    const ubicacionPedido = { lat, lng };
    const map = new google.maps.Map(document.getElementById("map"), {
        center: ubicacionPedido,
        zoom: 14,
    });

    new google.maps.Marker({
        position: ubicacionPedido,
        map: map,
        title: "Ubicación del pedido",
    });
}

document.getElementById("buscarBtn").addEventListener("click", () => {
    const numeroGuia = document.getElementById("numeroGuia").value;

    // Simulación de datos desde el backend
    if (numeroGuia === "12345") {
        const datosPedido = {
            nombre: "Juan Pérez",
            producto: "Electrodoméstico",
            destino: "Calle Falsa 123, Facatativá",
            conductor: "Carlos Ramírez",
            lat: 4.813671,
            lng: -74.354530, // Coordenadas simuladas
        };

        // Actualización de la información en pantalla
        document.getElementById("nombre").innerText = datosPedido.nombre;
        document.getElementById("producto").innerText = datosPedido.producto;
        document.getElementById("destino").innerText = datosPedido.destino;
        document.getElementById("conductor").innerText = datosPedido.conductor;

        // Mostrar el mapa con la ubicación
        initMap(datosPedido.lat, datosPedido.lng);
    } else {
        alert("Número de guía no encontrado. Por favor, intente nuevamente.");
    }
});
