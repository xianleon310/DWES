<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IMC</title>
</head>
<body>
    <?php
    //Obtiene el peso a través del método "GET" el cual recoge de la url así:
    // http://localhost:8082/imc.php?peso=80&altura=1.70
    if ($_GET["peso"] && $_GET["altura"]){
        $peso=$_GET["peso"];
        $altura=$_GET["altura"];
        $mensaje=calcular_imc($peso,$altura);
        echo "<h3> $mensaje </h3>";
    }else{
        //Si no se han puesto los parámetros como en el ejemplo, saltará el siguiente mensaje:
        echo "<h2>Parámetros no válidos</h2>";
    }
    function calcular_imc($peso, $altura){
        //pow es elevar (ya que el imc es => peso / altura elevado a 2)
        $imc=$peso/pow($altura,2);
        if ($imc <18.5){
            $mensaje="Bajo peso";
        }elseif($imc >=18.5 && $imc<25){
            $mensaje="Normal";
        }else{
            $mensaje="Sobrepeso";
        }
        return $mensaje;
    }
?>
</body>
</html>



