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
        else if(!(/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test($('.txtEmail').val())))
        {
            alert("El formato del correo no es válido");
            $('.txtEmail').focus();
        }
        else if($('.txtClave').val() == "")
        {
            alert("No ha especificado la clave");
            $('.txtClave').focus();
        }
        // validar con expresion regular regex que la clave
        // solo contenga letras y numeros
        else if(!(/^[a-zA-Z0-9]+$/.test($('.txtClave').val())))
        {
            alert("El formato de la clave no es correcto");
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