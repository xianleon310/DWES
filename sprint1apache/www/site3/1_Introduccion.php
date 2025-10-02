<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bienvenida</title>
</head>
<body>
    <?php
        function dar_bienvenida($nombre){
            echo ("<h2>Bienvenido $nombre </h2>");
        }
        dar_bienvenida("Xian");
    ?>
</body>
</html>