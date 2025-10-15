<?php
    $db=mysqli_connect('localhost','root','1234','mysitedb') or die('Fail');
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Base de datos</title>
</head>
<body>
    <h1>Conexion establecida</h1>
    <?php
        //Lanzar consulta
        $consulta='SELECT * FROM tJuegos';
        $resultado=mysqli_query($db,$consulta) or die ('Error de consulta');
        while ($row=mysqli_fetch_array($resultado)){
            echo $row['nombre'];
            echo "<br>";
            echo "<img width=100 height=100 src='";
            echo $row[2];
            echo "'></img>";
            echo "<br>";
        }    
    ?>
</body>
</html>