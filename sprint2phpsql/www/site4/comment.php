<?php
    #CODIGO PARA INSERTAR TUPLAS CADA VEZ QUE EL USUARIO LE DE A COMENTAR, TRAYENDO LO QUE EL USUARIO
    #ESCRIBE VÍA TECLADO Y EL ID DEL GET
    $db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
    $juego_id = $_POST['juego_id'];
    $comentario = $_POST['new_comment'];
    $query = "INSERT INTO tComentarios(comentario, juego_id) VALUES ('".$comentario."', ".$juego_id.")";
    mysqli_query($db, $query) or die('Error al insertar comentario');
    echo "<p>Nuevo comentario añadido correctamente</p>";
    echo "<a href='/detail.php?id=" . $juego_id . "'>Volver al juego</a>";
    mysqli_close($db);
?>