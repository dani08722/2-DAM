$(document).ready(function () {

    $("#anadir-fila").on("click", function () {
        $("#tabla-ejemplo tbody").append(
            "<tr>" +
            "<td>Nuevo</td>" +
            "<td>25</td>" +
            "<td>PMDM</td>" +
            "<td>Nuevo</td>" +
            "</tr>"
        );
    });

    $("#anadir-columna").on("click", function () {
        $("#tabla-ejemplo tbody tr").append("<td>Nuevo</td>");
        $("#tabla-ejemplo thead tr").append("<th>Nuevo</th>");
    });

    $("#eliminar-fila").on("click", function () {
        $("#tabla-ejemplo tbody tr:last").remove();
    });

    $("#eliminar-columna").on("click", function () {
        $("#tabla-ejemplo tbody tr td:last").remove();
        $("#tabla-ejemplo thead tr th:last").remove();
    });

    $("#eliminar-tabla").on("click", function () {
        $("#tabla-ejemplo").remove();
    });
});