
$("input:checkbox.check").each(function (){
    var list_check =($(this).checked ? $(this).val():"");
    alert(list_check);
});

$(document).click(function comprobar() {
    if($(this).is(':checked')) {
        alert('Sim');
      }
    else {
        alert('no')
        mycheck= $(this).val.val();
        alert(mycheck);
      }
});


