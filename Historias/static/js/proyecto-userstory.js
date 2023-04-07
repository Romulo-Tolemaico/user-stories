function crearHistoria() {
    let crearhistoria = document.getElementById('crearhistoria');
    console.log(crearhistoria.classList);
    crearhistoria.classList.remove("invisible");
}

function cerrarCrearhistoria() {
    let crearhistoria = document.getElementById('crearhistoria');
    crearhistoria.classList.add("invisible");
}

function propiedades() {
    let crearhistoria = document.getElementById('crearpropiedades');
    crearhistoria.classList.remove("invisible");
}

function abrirEditar() {
    let abrirModal = document.getElementById("editarhistoria");
    abrirModal.classList.remove("invisible");
}
function propiedadesEliminar() {
    let eliminarhistoria = document.getElementById('eliminar');
    eliminarhistoria.classList.remove("invisible");
}

function cerrarEliminar() {
    let crearpropiedades = document.getElementById('crearpropiedades');
    crearpropiedades.classList.add("invisible");
}

function abrirModal(idModal) {
    let abrirModal = document.getElementById(idModal);
    abrirModal.classList.remove("invisible");
}

function cerrarModal(idModal) {
    let modal = document.getElementById(idModal);
    modal.classList.add("invisible");
}