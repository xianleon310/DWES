<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Tabla</title>
    </head>
    <body>
        <table>
            <tr>
                <td>Operación</td>
                <td>Resultado</td>
            </tr>
            <?php
                for ($i=1;$i<=10;$i++){
                    $resultado=7*$i;
                    echo "<tr>";
                    echo "<td>7x" . $i . "</td>";
                    echo "<td>" . $resultado . "</td>";
                    echo "</tr>";
                }
            ?>
        </table>
    </body>
</html>