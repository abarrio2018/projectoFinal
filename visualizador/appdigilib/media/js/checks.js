
$("input:checkbox.check").each(function (){
    var list_check =($(this).checked ? $(this).val():"");
    alert(list_check);
});

$(document).ready(function comprobar() {

      if($(this).is(":checked")) {
         alert('Sim');
      } else {
          mycheck= $(this).text();
          alert(mycheck);
      }
   });
});

"""$('#btn1').click(function() {
    console.log("click");
    a=$('#inputA').val();
    b=$('#inputB').val();
    $.ajax({
        method: 'POST',
        url: 'ruta de tu vista definida en django'
        data: {
            'a': a,
            'b': b, 
        },
        dataType: "json",
        success: function(response) {
            $('#outputR').val(response.resultado);
        }
    }); 
});"""
