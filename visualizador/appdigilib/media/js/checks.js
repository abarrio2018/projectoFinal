
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
