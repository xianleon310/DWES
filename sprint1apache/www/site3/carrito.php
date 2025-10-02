<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Carrito</title>
</head>
<body>
    <?php
        //Creamos array asociativo (cada elemento tiene un valor)
        $productos=[
            "manzana" => 0.5,
            "pan" => 1.2,
            "leche" => 0.95,
            "huevos" => 2.3,
            "aceite" => 4.5,
            "arroz" => 1.8
        ];
        $total=0;
        echo "<table><tr><td>Producto</td><td>Precio</td></tr>"; //primera fila (la principal)
        //Recorremos el vector asociativo dandole a cada elemento "$producto" y su correspondiente valor como "$precio" 
        foreach($productos as $producto => $precio){
            echo "<tr>";
            echo "<td>" . $producto . "</td>";
            echo "<td>" . $precio . "</td>";
            echo "</tr>";
            $total=$total+$precio;
        }
        echo "<tr>";
        echo "<td>TOTAL</td>";
        echo "<td>" . $total . "</td>";
        echo "</tr>";
        echo "</table>";

    ?> 
</body>
</html>
