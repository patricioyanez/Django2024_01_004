$(function(){

    $('.btnLimpiar').click(function(){
        $('.txtEmail, .txtClave').val('');
        $('.txtEmail').focus();
    })

    $('.btnEnviar').click(function(){
        if($('.txtEmail').val() == "")
        {
            alert("No ha especificado el correo");
            $('.txtEmail').focus();
        }
        else if($('.txtClave').val() == "")
        {
            alert("No ha especificado la clave");
            $('.txtClave').focus();
        }
        else
        {
            alert("La información enviada es: \n" +
                    "Correo: " + $('.txtEmail').val() +
                    "\nClave : " + $('.txtClave').val()
                )
        }
    })
})