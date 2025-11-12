<?php
    $db=mysqli_connect('localhost','root','1234','mysitedb') or die('Fail');
    if (!empty($_POST["nombre"]) && !empty($_POST["mail"]) && !empty($_POST["apel"]) && !empty($_POST["pass"]) && !empty($_POST["pass2"])){
        $nombre=$_POST["nombre"];
        $apellidos=$_POST["apel"];
        $mail=$_POST["mail"];
        $contra=$_POST["pass"];
        $contra2=$_POST["pass2"];
        //COMPROBAR SI EL EMAIL YA EXISTE:
        $consulta_email=$db->prepare("SELECT * FROM tUsuarios WHERE email=?");
        $consulta_email->bind_param("s", $mail);
        $consulta_email->execute();
        $resultado_email = $consulta_email->get_result();
        if (mysqli_num_rows($resultado_email)>0){
            echo "Error: este email ya está registrado";
            echo "<a href='register.html'>Volver al registro</a>";
        // COMPROBAR SI LAS CONTRASEÑAS COINCIDEN
        } elseif ($contra !== $contra2) {
            echo "Error: las contraseñas no coinciden";
            echo "<br><a href='register.html'>Volver al registro</a>";
        }else{
            //CIFRAR CONTRASEÑA
            $contraseña_cifrada=password_hash($contra,PASSWORD_DEFAULT);
            
            //ESTÁ TODO CORRECTO
            //INSERTAR LOS DATOS RECOGIDOS EN EL FORMULARIO A LA BASE DE DATOS
            $insertar_usuarios = $db->prepare("INSERT INTO tUsuarios (nombre, apellidos, email, contraseña) VALUES (?, ?, ?, ?)");
            $insertar_usuarios->bind_param("ssss", $nombre, $apellidos, $mail, $contraseña_cifrada);
            $insertar_usuarios->execute();
            header('Location: login.html');
        }
    }else{
        echo "Faltan campos por cubrir";
        echo "<br><a href='register.html'>Volver al registro</a>";
    }
?>