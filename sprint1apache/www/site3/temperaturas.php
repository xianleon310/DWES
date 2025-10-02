<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Temperaturas</title>
</head>
<body>
<!-- Creamos un formulario con un método POST (importante) -->
<form action="temperaturas.php" method="post">
    <label>Cantidad:</label><br>
    <!-- El "name"de cada input es el que estará asociado a php cuando se nombren (asociado a la variable), 
     y el "value" estará asociado al valor de dicha variable-->
    <input type="number" name="cantidad"><br><br>
    
    <input type="radio" name="conversion" value="c_to_f">
    <label>Celsius → Fahrenheit</label><br>
    
    <input type="radio" name="conversion" value="f_to_c">
    <label>Fahrenheit → Celsius</label><br><br>
    
    <input type="submit" value="Convertir">
</form>
<?php
    if (isset($_POST["cantidad"]) && isset($_POST["conversion"])) {
    //SE GUARDA EN LAS VARIABLES EL VALOR DEL POST DEL CAMPO "name" DE LOS INPUT
    $cantidad=$_POST["cantidad"];
    $conversion=$_POST["conversion"];
    //SI EL VALOR ES IGUAL A "f_to_c" SITUADO EN EL VALUE SE HARÁ LA OPERACIÓN
    if ($conversion === "f_to_c"){
        $celsius=(($cantidad-32)*5)/9;
        echo "<p> Equivalen a " . $celsius . " °C</p>";
    }else{
        $fahrenheit=(($cantidad*9)/5)+32;
        echo "<p> Equivalen a " . $fahrenheit . " °F</p>";
    }
    }
?>
</body>
</html>