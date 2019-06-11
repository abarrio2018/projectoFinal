
$("#check1").onclick(function (){
    if( $("#check1").is(':checked'))
        alert('si');
    else
        alert('no');
});

$(document).ready(function comprobar() {
   $(document).on('click', '#check1', function () {
      if($(this).is(":checked")) {
         alert('Sim');
      } else {
         alert('Não');
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
