<!DOCTYPE html>
<html lang="pt-br">
  <head>
    <meta charset="utf-8">
    <title>Intâncias</title>
  </head>
  <body>
    <?php
    require_once 'usuario.php';
    //DAO Data Access Object (em português Objeto de acesso a dados)
    //DAO é uma classe construida para interagir com o banco de dados

    //Essa classe herda métodos do comando sql, que por sua vez, herda os métodos da classe PDO
    $usuario = new Usuario;

    $usuario->inserir('Tevert',22,'Masculino',93534170,'eudson.duraes@gmail.com');
    ?>
  </body>
</html>
