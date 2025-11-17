<?php
    $db=mysqli_connect('172.16.0.2','root','1234','mysitedb') or die('Fail');
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
    <?php
        if ($_GET["id"]){
            $id=$_GET["id"];
        }else{
            die ("<h3 class='rojo'>No se ha especificado ningún ID</h3>");
        }

        //Lanzar consultas
        $consultatJuegos = $db->prepare('SELECT * FROM tJuegos WHERE id = ?');
        $consultatJuegos->bind_param("i", $id);
        $consultatJuegos->execute();
        $resultadotJuegos = $consultatJuegos->get_result() or die ('Error de consulta');
        $row = $resultadotJuegos->fetch_array();

        $consultatComentarios = $db->prepare("SELECT comentario, fecha FROM tComentarios WHERE juego_id = ?");
        $consultatComentarios->bind_param("i", $id);
        $consultatComentarios->execute();
        $resultadotComentarios = $consultatComentarios->get_result() or die("Error al consultar comentarios");

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
            echo "<li>" . $com['comentario'] . " - <small>(" . $com['fecha'] . ")</small></li>";
        }
        echo "</ul>";   
    ?>
    <p>Deja un nuevo comentario:</p>
    <!--Se hace un formulario, el cual la lógica va a /comment.php-->
    <form action="comment.php" method="post">
        <!--para referenciarlo en la logica de post, se utilizará el new_comment, y el value 
            será lo que se quedará la lógica (lo que el usuario ponga por teclado)-->
        <textarea rows="4" cols="50" name="new_comment"></textarea><br>
        <!--para referenciarlo en la logica de post, se utilizará el juego_id, y el value será
            lo que se quedará la lógica (el 'echo $id') que hace referencia al id donde estamos-->
        <input 
            type="hidden" 
            name="juego_id" 
            value="
                <?php 
                    echo $id;
                ?>
            ">
        <input type="submit" value="Comentar">
    </form>
    <a href="logout.php">Cerrar sesión</a>
    <br><br>
    <a href="main.php">Volver a la página principal</a>
</body>
</html>