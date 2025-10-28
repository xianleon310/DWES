<?php
    //CIERRA LA SESIÓN Y REDIRIGE A LOGIN
    session_start();
    session_destroy();
    header('Location: login.html');
?>