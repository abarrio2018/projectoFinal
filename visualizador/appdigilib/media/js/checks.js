$(document).ready(function() {

    $('.check_cat').change(function() {
        ajax_post_categorias();
    });


    $('.check_task').change(function() {
        ajax_post_tareas();
    });


    $('#Modal').on('shown.bs.modal', function(event) {
        id_article = event.relatedTarget.id;
        var modal = $(this);

        $.ajax({
            beforeSend: function(xhr, settings) {
          var csrftoken = getCookie('csrftoken');
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
          },
            type:'POST',
            url:'detail/',
            dataType: 'html',
            data: {
              'id_article': id_article,

              },
            success: function(response){
              modal.find('.modal-body').html(response);

            },
            error: function(xhr, status, error) {
                alert("This article is not exist.");
            }
        });

    });


function getCookie(name) {

    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {

        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }

    }

    return cookieValue;
};

async function ajax_post_tareas(){
     var lista_task = [];
        $( '.check_task' ).each(function( index ) {
            if(this.checked) {
                lista_task.push($(this).attr('name'));
            }
            else{

            }
        });
        //var csrf;
        $.ajax({
            beforeSend: function(xhr, settings) {
          var csrftoken = getCookie('csrftoken');
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
          },
            type:'POST',
            url:'index/c2',
            dataType: 'html',
            data: {
              'lista': lista_task,
              },
            success: function(json){
              $('#content1').html(json);
                
            },
            error: function(xhr, status, error) {
                alert("error");
            }
        });
    };

async function ajax_post_categorias() {
    var list_marcados = [];

        $( '.check_cat' ).each(function( index ) {
            if(this.checked) {
                list_marcados.push($(this).attr('name'));

            }
            else{
                //lista_cat_des.push($(this).attr('name'));

            }
        });
        //var csrf;
        $.ajax({
            beforeSend: function(xhr, settings) {
            var csrftoken = getCookie('csrftoken');
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
          },
            type:'POST',
            url:'index/c1',
            dataType:'html',
            data: {
                //'lista_c': lista_cat_des,
                'lista': list_marcados,

            },
            success: function(json){
                $('#content1').html(json);
            },
            error: function(xhr, status, error) {
                alert("error");
            }
        });

    };
});