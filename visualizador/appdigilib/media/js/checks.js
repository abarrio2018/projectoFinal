

var aChk = document.getElementsByName('check');

function verificaChecks() {

    for (var i=0;i<aChk.length;i++){

        if (aChk[i].checked){
            //Aqui eu teria que atribuir '1'
            categoria = aChk[i].value;
            alert(aChk[i].id + ' = ' + aChk[i].value + " marcado.");
        }
    }
}
