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
        if ($_GET["id"]){
            $id=$_GET["id"];
        }else{
            die ("<h3 class='rojo'>No se ha especificado ningún ID</h3>");
        }

        //Lanzar consultas
        $consultatJuegos='SELECT * FROM tJuegos WHERE id='.$id;
        $resultadotJuegos=mysqli_query($db,$consultatJuegos) or die ('Error de consulta');
        $row=mysqli_fetch_array($resultadotJuegos);
        $consultatComentarios = "SELECT comentario FROM tComentarios WHERE juego_id = $id";
        $resultadotComentarios = mysqli_query($db, $consultatComentarios) or die("Error al consultar comentarios");

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
        echo "<p class='rojo'>Comentarios:</p>";
        //Mostrar todos los comentarios relacionados con ese id de juego
        echo "<ul>";
        while ($com = mysqli_fetch_array($resultadotComentarios)) {
            echo "<li>" . $com['comentario'] . "</li>";
        }
        echo "</ul>";   
    ?>
</body>
</html>