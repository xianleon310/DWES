<?php
    if ($_GET["peso"] && $_GET["altura"]){
        $peso=$_GET["peso"];
        $altura=$_GET["altura"];
        $resultado=calcular_imc($peso,$altura);
        echo $resultado;
    }else{
        echo "Parámetros no válidos";
    }
    function calcular_imc($peso, $altura){
        $imc=$peso/pow($altura,2);
        if ($imc <18.5){
            $mensaje="Bajo peso";
        }elseif($imc >=18.5 && $imc<25){
            $mensaje="Normal";
        }else{
            $mensaje="Sobrepeso";
        }
        return $mensaje;
    }
?>