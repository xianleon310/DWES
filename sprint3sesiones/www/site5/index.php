<?php
session_start();

//SI HAY SESIÓN ACTIVA VAMOS AL MAIN
if (!empty($_SESSION['user_id'])) {
    header('Location: main.php');
} else {
    // SI NO, A LOGIN
    header('Location: login.html');
}
?>