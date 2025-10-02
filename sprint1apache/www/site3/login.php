<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <h1>LOGIN</h1>
    <form method="post">
        <p>
            <input type="text" name="user">
        </p>
        <p>
            <input type="password" name="password">
        </p>
        <input type="submit" value="Acceder">
        <?php
            if (isset($_POST["user"]) && isset($_POST["password"])){
                $user=$_POST["user"];
                $password=$_POST["password"];
                if ($user!="admin" || $password!="1234"){
                    echo "<h2>Acceso denegado</h2>";
                }else{
                    echo "<h2>Acceso concedido</h2>";
                }
            }
        ?>
    </form>
</body>
</html>