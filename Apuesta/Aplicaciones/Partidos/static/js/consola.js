(function() {
    const btnApuesta = document.querySelectorAll(".btnApuesta");

    btnApuesta.forEach(btn=>{
        btn.addEventListener("click",(e)=>{
            const confirmacion = confirm('¿Seguro que quieres apostar?');
            if(!confirmacion){
                e.preventDefault();
            }
        });
    });

})();
