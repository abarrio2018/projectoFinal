$(document).ready(function() {

    $('.check_cat').change(function() {

        var lista_cat = [];
        $( '.check_cat' ).each(function( index ) {
            if(this.checked) {
                //alert("si");
            }
            else{
                //alert($(this).attr('name'));
                lista_cat.push($(this).attr('name'));
                //alert(lista_cat);
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

        ajax_post();

    });


async function ajax_post(){

     var lista_task = [];
        $( '.check_task' ).each(function( index ) {

            if(this.checked) {
            }
            else{
                lista_task.push($(this).attr('name'));
            }

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
              }
        var csrf;

        $.ajax({
            beforeSend: function(xhr, settings) {
              
          var csrftoken = getCookie('csrftoken');
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
          },
    
            type:'POST',
            url:'index/c1',
            dataType: 'json',
            data: {
              'lista': lista_task,
              },
            success: function(json)
            {
              alert('suceso')
                
            },
            error: function(xhr, status, error) {
              
            }
        });
}

});