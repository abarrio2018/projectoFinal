
$(document).click(function comprobar() {
    if($(this).is(':checked')) {
        alert('Sim');
      }
    else {
        alert('no')
        mycheck= $(this).text($(this));
        alert(mycheck);
      }
});

