function Sumar() {
    var x;
    var y;
    var z = parseInt(document.getElementById("numero1").value) + parseInt(document.getElementById("numero2").value);
    document.getElementById("Suma").innerHTML = "El resultado de la suma es:" + z;
}
function Multiplicar() {
    var x;
    var y;
    var z = parseInt(document.getElementById("numero1").value) * parseInt(document.getElementById("numero2").value);
    document.getElementById("Suma").innerHTML = "El resultado de la multiplicacion es:" + z;
}