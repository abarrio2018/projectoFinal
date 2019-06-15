$(document).ready(function() {

    $('.check_task').change(function() {

        var lista_task = [];
        $( '.check_task' ).each(function( index ) {

            if(this.checked) {
                alert("si");
            }
            else{
                alert($(this).attr('name'));
                lista_task.push($(this).attr('name'));
                alert(lista_task);
            }

        });

    });

    $('.check_cat').change(function() {

        var lista_cat = [];
        $( '.check_cat' ).each(function( index ) {
            if(this.checked) {
                alert("si");
            }
            else{
                alert($(this).attr('name'));
                lista_cat.push($(this).attr('name'));
                alert(lista_cat);
            }

        });
    });

});