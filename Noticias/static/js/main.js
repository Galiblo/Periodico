(function () {

    const btnEliminacion = document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Seguro de eliminar esta noticia?');
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });

})();