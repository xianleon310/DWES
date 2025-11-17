<?php
    #CODIGO PARA INSERTAR TUPLAS CADA VEZ QUE EL USUARIO LE DE A COMENTAR, TRAYENDO LO QUE EL USUARIO
    #ESCRIBE VÍA TECLADO Y EL ID DEL GET
    $db = mysqli_connect('172.16.0.2', 'root', '1234', 'mysitedb') or die('Fail');
    //SE INICIA LA SESIÓN DE PARTE DE LOGIN
    session_start();
    $user_id_a_insertar=NULL;
    //SE RECOGE EL ID QUE SE GUARDO EN EL LOGIN (EN CASO CONTRARIO SE MANTENDRÁ EN NULL Y EL COMENTARIO SERÁ ANÓNIMO)
    if (!empty($_SESSION["user_id"])){
        $user_id_a_insertar=$_SESSION["user_id"];
    }
    $juego_id = $_POST['juego_id'];
    $comentario = $_POST['new_comment'];
    $query = $db->prepare("INSERT INTO tComentarios(comentario, juego_id, usuario_id) VALUES (?, ?, ?)");
    $query->bind_param("sii", $comentario, $juego_id, $user_id_a_insertar);
    $query->execute() or die('Error al insertar comentario');
    echo "<p>Nuevo comentario añadido correctamente</p>";
    echo "<a href='detail.php?id=" . $juego_id . "'>Volver al juego</a>";
    mysqli_close($db);
?>