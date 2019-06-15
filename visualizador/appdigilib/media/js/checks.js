$(document).ready(function() {

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
        $.ajax({
            type:'POST',
            url:'',
            dataType: 'json',
            //headers: {"X-CSRFToken": $.cookie("csrftoken")},
            data: {lista_cat,
                csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function(json)
            {
                //specifying a dataType of json makes jQuery pre-eval the response for us
                console.log(json.message);
            }
        });
    });
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

        $.ajax({
            type:'POST',
            url:'',
            dataType: 'json',
            //headers: { "X-CSRFToken": $.cookie("csrftoken")},
            data: {lista_task,
                csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function(json)
            {
                //specifying a dataType of json makes jQuery pre-eval the response for us
                console.log(json.message);
            }
        });

    });


});