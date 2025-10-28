<?php
    $db=mysqli_connect('localhost','root','1234','mysitedb') or die('Fail');
    //NO SE COMPRUEBA QUE FALTAN CAMPOS, YA QUE HAY CODIGO DE JS EN EL HTML COMPROBANDOLO
    $mail=$_POST["mail"];
    $contra=$_POST["pass"];
    //COMPROBAR SI EL EMAIL EXISTE PARA HACER LOGIN:
    $consulta_email = $db->prepare("SELECT id, contraseña FROM tUsuarios WHERE email = ?");
    //"s" PORQUE EL CAMPO 'contraseña' ES STRING (EL CAMPO 'id' NO SE CUENTA)
    $consulta_email->bind_param("s", $mail);
    $consulta_email->execute();
    $resultado_email = $consulta_email->get_result();
    //SI HAI ALGUNA FILA AFECTADA (>0)....
    if ($resultado_email-> num_rows>0){
        //SE OBTIENE EL OBJETO DE LA TUPLA EL CUAL SU EMAIL COINCIDE CON EL EMAIL DE LA BASE DE DATOS
        $tupla_contra=$resultado_email->fetch_array();
        //SE COMPARA EL CAMPO DE LA TUPLA OBTENIDA DE LA BASE DE DATOS (tupla_contra[1]) CON LA CONTRASEÑA QUE HEMOS PUESTO
        if (password_verify($contra,$tupla_contra[1])){
            //INICIA SESIÓN CON EL USUARIO (COGIDO EN LA POSICION 0 DEL SELECT)
            session_start();
            $_SESSION['user_id']=$tupla_contra[0];
            //REDIRIGE A main.php
            header('Location: main.php');
        }else{
            echo "Contraseña incorrecta";
            echo "<br><a href='login.html'>Volver al login</a>";
        }
    } else{
        echo "No se ha encontrado ninguna cuenta con ese correo electrónico.";
        echo "<br><a href='login.html'>Volver al login</a>";
    }
?>