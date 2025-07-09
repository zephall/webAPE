   let map = L.map('map').setView([19.4161, -98.9026], 14); // Chicoloapan

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; OpenStreetMap contributors'
        }).addTo(map);

        let marker;

        map.on('click', function (e) {
            const lat = e.latlng.lat.toFixed(6);
            const lng = e.latlng.lng.toFixed(6);
            document.getElementById('latitud').value = lat;
            document.getElementById('longitud').value = lng;

            if (marker) {
                marker.setLatLng(e.latlng);
            } else {
                marker = L.marker(e.latlng).addTo(map);
            }
        });

        function verificarUbicacion() {
            const lat = document.getElementById("latitud").value;
            const lng = document.getElementById("longitud").value;
            if (!lat || !lng) {
                alert("Por favor selecciona una ubicación en el mapa.");
                return false;
            }
            return true;
        }