<?php
    $productos=[
        "manzana" => 0.5,
        "pan" => 1.2,
        "leche" => 0.95,
        "huevos" => 2.3,
        "aceite" => 4.5,
        "arroz" => 1.8
    ];
    $total=0;
    echo "<table><tr><td>Producto</td><td>Precio</td></tr>";
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