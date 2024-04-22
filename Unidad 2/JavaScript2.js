
document.getElementById("txtNombre").value= "Anita";


function sumar()
{
    let numero1 = 1;
    let numero2 = 500;
    let resultado = numero1 + numero2;
    alert("El resultado es :" + resultado);
}
function sumar2(numero1, numero2)
{
    let resultado = numero1 + numero2;
    alert("El resultado es :" + resultado);
}

function sumar3()
{
    let n = document.getElementById("txtNumero1").value;
    let m = document.getElementById("txtNumero2").value;
    alert("La suma es: " + (Number(n)+Number(m)))
}
function restar()
{
    let n = document.getElementById("txtNumero1").value;
    let m = document.getElementById("txtNumero2").value;
    alert("La suma es: " + (Number(n)-Number(m)))
}

window.onload = function (){
    document.getElementById("txtApellido").value="Fernandez";
}