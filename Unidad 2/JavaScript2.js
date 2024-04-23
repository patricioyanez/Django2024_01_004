document.getElementById("txtNombre").value="Ana";

function sumar()
{
    let n1 = 10;
    let n2 = 20;
    let res = n1 + n2;
    alert("El resultado es: " + res);
}
function sumar2(n1, n2) 
{
    let res = n1 + n2;
    alert("El resultado es: " + res);
}
function sumar3()
{
    let n1 = document.getElementById("txtNumero1").value;
    let n2 = document.getElementById("txtNumero2").value;
    let res = Number(n1) + Number(n2);
    alert("El resultado es: " + res);
}