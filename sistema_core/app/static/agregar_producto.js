document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("form-agregar");
    const codigoInput = document.getElementById("codigo");
    const modal = new bootstrap.Modal(document.getElementById("confirmarCodigoModal"));
    const confirmarBtn = document.getElementById("confirmar-generacion");

    let modalYaMostrado = false;  // Para evitar múltiples asignaciones

    form.addEventListener("submit", function (e) {
        if (codigoInput && codigoInput.value.trim() === "") {
            if (!modalYaMostrado) {
                e.preventDefault(); // Detener envío
                modal.show();
                modalYaMostrado = true;

                confirmarBtn.addEventListener("click", function () {
                    const hiddenInput = document.createElement("input");
                    hiddenInput.type = "hidden";
                    hiddenInput.name = "generar_codigo";
                    hiddenInput.value = "1";
                    form.appendChild(hiddenInput);

                    modal.hide();
                    form.submit();
                }, { once: true });  // 🔥 Se asegura que no se agregue más de un listener
            } else {
                e.preventDefault(); // Ya está mostrando el modal, evitar doble envío
            }
        }
    });
});
