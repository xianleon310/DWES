<?php
    $db=mysqli_connect('localhost','root','1234','mysitedb') or die('Fail');
    session_start();
    $nombre_usuario="Invitado";
    //SI HAY ALGUIEN LOGEADO.. (RECORDAR QUE EN EL LOGIN SE ACTIVA)
    if (!empty($_SESSION["user_id"])){
        //SE RECOGE EL NOMBRE DEL USUARIO LOGEADO (SE MOSTRARÁ COMO BIENVENIDA)
        $consulta_usuario = $db->prepare("SELECT nombre FROM tUsuarios WHERE id = ?");
        $consulta_usuario->bind_param("i", $_SESSION["user_id"]);
        $consulta_usuario->execute();
        $resultado_usuario = $consulta_usuario->get_result();
        $tupla_nombre = $resultado_usuario->fetch_array();
        $nombre_usuario=$tupla_nombre[0];
    }
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
        //MENSAJE BIENVENIDA
        echo "<h1>Bienvenido, ".$nombre_usuario."</h1>";
        //Lanzar consulta
        $consulta='SELECT * FROM tJuegos';
        $resultado=mysqli_query($db,$consulta) or die ('Error de consulta');
        //Bucle recorriendo todas las filas y plasmandolo
        while ($row=mysqli_fetch_array($resultado)){
            echo "<div class='juego'>";
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
            echo "<br><br>";
            echo "<a href='detail.php?id=" . $row['id'] . "'>Ver detalles</a>"; 
            echo "</div>";
        }
        echo "<br>";
        if (!empty($_SESSION['user_id'])) {
            // SI EL USUARIO ESTÁ LOGEADO MUESTRA ESTO
            echo '<a href="change_password.html">Cambiar contraseña</a><br><br>';
            echo '<a href="logout.php">Cerrar sesión</a>';
        } else {
            // SI EL USUARIO NO ESTÁ LOGEADO MUESTRA ESTO
            echo '<a href="login.html">Iniciar sesión</a><br><br>';
            echo '<a href="register.html">Registrarse</a>';
        }
    ?>
</body>
</html>