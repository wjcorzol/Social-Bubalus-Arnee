var dashboard = document.getElementById("areaDeGraficas");
var papel = dashboard.getContext("2d");

var grafica = {
    url: "Imagenes/dashboard.png",
    cargaOK: false
}

grafica.imagen = new Image();
grafica.imagen.src = grafica.url;
grafica.imagen.addEventListener("load", cargarGrafica);

function cargarGrafica()
{
    grafica.cargaOK = true;
    dibujar();
}

function dibujar()
{
    if(grafica.cargaOK)
    {
        papel.drawImage(grafica.imagen, 0, 0);
    }
}