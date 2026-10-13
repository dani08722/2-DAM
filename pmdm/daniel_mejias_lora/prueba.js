var contNota = 1;
var notaSeleccionada = null;

// cuando pulsas Añadir, se vuelve a dejar el formulario vacío para la siguiente
$("#anadirNota").on("click", function () {
    notaSeleccionada = null;
    $("#tituloNota").val("");
    $("#anchoNota").val("4");
    $("#colorNota").val("danger");
});

// Al pulsar Editar, se cargan los datos de esa tarjeta en el modal
$("#contenedorNotas").on("click", ".editar-nota", function () {
    notaSeleccionada = $(this).closest(".columna-nota");
    $("#tituloNota").val(notaSeleccionada.attr("data-titulo"));
    $("#anchoNota").val(notaSeleccionada.attr("data-ancho"));
    $("#colorNota").val(notaSeleccionada.attr("data-color"));
});

// Guardar una nota nueva o guardar los cambios de una nota.
$("#guardarNota").on("click", function () {
    var titulo = $("#tituloNota").val();
    var ancho = $("#anchoNota").val();
    var color = $("#colorNota").val();

    if (titulo == "") {
        $("#guardarNota").attr("data-bs-dismiss", "");
        alert("Escribe el título de la nota");
        return;
    }

    $("#guardarNota").attr("data-bs-dismiss", "modal");

    if (notaSeleccionada == null) {
        var nuevaNota = crearNota(contNota, titulo, ancho, color);
        $("#contenedorNotas").append(nuevaNota);
        contNota++;
    } else {
        var numero = notaSeleccionada.attr("data-numero");
        notaSeleccionada.remove();
        var notaEditada = crearNota(numero, titulo, ancho, color);
        $("#contenedorNotas").append(notaEditada);
        notaSeleccionada = null;
    }
});

// Eliminar
$("#contenedorNotas").on("click", ".eliminar-nota", function () {
    $(this).closest(".columna-nota").remove();
});

// Crea el HTML de una tarjeta con las opciones elegidas.
function crearNota(numero, titulo, ancho, color) {
    var colorTexto = "text-white";

    if (color == "warning") {
        colorTexto = "text-dark";
    }

    return `<div class="col-12 col-md-${ancho} columna-nota"
                data-numero="${numero}"
                data-titulo="${titulo}"
                data-ancho="${ancho}"
                data-color="${color}">
        <div class="card h-100">
            <div class="card-header bg-${color} ${colorTexto} d-flex justify-content-between align-items-center">
                <span>Nota ${numero}</span>
                <div>
                    <button type="button" class="btn btn-sm btn-primary border-grey border border-2  editar-nota"
                        data-bs-toggle="modal" data-bs-target="#modalNota">Editar</button>
                    <button type="button" class="btn btn-sm btn-danger border border-2 border-grey eliminar-nota">Eliminar</button>
                </div>
            </div>
            <div class="card-body">
                <p class="card-text">${titulo}</p>
            </div>
        </div>
    </div>`;
}
