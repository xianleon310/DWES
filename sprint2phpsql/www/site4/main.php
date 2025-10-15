<?php
    $db=mysqli_connect('localhost','root','1234','mysitedb') or die('Fail');
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Base de datos</title>
    <link rel="stylesheet" href="main-estilos.css">
</head>
<body>
    <h1>Conexión establecida</h1>
    <?php
        //Lanzar consulta
        $consulta='SELECT * FROM tJuegos';
        $resultado=mysqli_query($db,$consulta) or die ('Error de consulta');
        //Bucle recorriendo todas las filas y plasmandolo
        while ($row=mysqli_fetch_array($resultado)){
            echo "<h2>";
            echo $row['nombre'];
            echo "</h2>";
            echo "<img width=100 height=100 src='";
            echo $row[2];
            echo "'></img>";
            echo "<p><em>";
            echo $row['descripcion'];
            echo "</em></p>";
            echo $row['plataforma'];
            echo "<br>";
            echo "<a href='detail.php?id=" . $row['id'] . "'>Ver detalles</a>";
            echo "<hr>"; 

        }    
    ?>
</body>
</html>