<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora</title>
</head>
<body>
    <label>Introduce dos números: </label>
    <form method="post">
        <p>
            <input type="text" name="num1">
            <select name="opciones">
                <option value="" selected disabled>Selecciona una operación</option>
                <option value="sumar">Sumar</option>
                <option value="restar">Restar</option>
                <option value="multiplicar">Multiplicar</option>
                <option value="dividir">Dividir</option>
            </select>
            <input type="text" name="num2">
        </p>
        <input type="submit" value="Resultado">
    </form>
    <h2>
    <?php
        if (!empty($_POST["num1"]) && !empty($_POST["num2"]) && !empty($_POST["opciones"])) {
            $num1=$_POST["num1"];
            $num2=$_POST["num2"];
            $opciones=$_POST["opciones"];
            
            switch($opciones){
                case "sumar":
                    
                    echo "$num1 + $num2 = ".$num1+$num2;
                    break;
                case "restar":
                    echo "$num1 - $num2 = ".$num1-$num2;
                    break;
                case "multiplicar":
                    echo "$num1 * $num2 = ".$num1*$num2;
                    break;
                case "dividir":
                    echo "$num1 / $num2 = ".$num1/$num2;
                    break;
            }
            
                

        }else if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            echo "Faltan parámetros";
        }
    ?>
    </h2>
</body>
</html>