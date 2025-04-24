function initMap() {

    const ubicacionInicial = { lat: 4.710989, lng: -74.072092 }; 
    const map = new google.maps.Map(document.getElementById("map"), {
        center: ubicacionInicial,
        zoom: 14,
    });

    // Marcador de entrega
    new google.maps.Marker({
        position: ubicacionInicial,
        map: map,
        title: "Próxima entrega",
    });
}

window.onload = initMap;
