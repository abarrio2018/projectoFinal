$(document).ready(function() {

    $('.check').change(function() {

        $( '.check' ).each(function( index ) {
            var lista_check = [];
            if(this.checked) {
                alert("si")
            }
            else{
                alert("no");
                var lista_check = lista_check.add( $(this).val());

                $.ajax({
                    type:"POST",
                    url:"index/",
                    data: lista_check
                });


            }
            alert(lista_check);
        });
    });
})