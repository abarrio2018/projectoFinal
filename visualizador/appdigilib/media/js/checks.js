
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
