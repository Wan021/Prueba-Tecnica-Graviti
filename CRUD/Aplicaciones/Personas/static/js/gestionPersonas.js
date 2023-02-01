(function(){
    const btnEliminacion = document.querySelectorAll(".btnEliminacion");
    const btnCancel = document.querySelectorAll(".btnCancel");

    btnEliminacion.forEach(btn=>{
        btn.addEventListener('click',(e)=>{
            const confirmacion = confirm('¿Seguro de eliminar a esta persona?');
            if(!confirmacion){
                e.preventDefault();
            }
        });
    });

    btnCancel.forEach(btn=>{
        btn.addEventListener('click',(e)=>{
            const confirmacion = confirm('¿Seguro de cancelar?');
            if(!confirmacion){
                e.preventDefault();
            }
        });
    });
    

})();