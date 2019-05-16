<!DOCTYPE html>
<html lang="PT-BR">
  <head>
    <meta charset="utf-8">
    <title>Criando objetos</title>
  </head>
  <body>
    <pre>
    <?php
    require_once 'Classes.php';

    $pessoa1 = new contas();
    $pessoa2 = new contas();

    $nome = $_GET["nome"];

    $pessoa1->definirNome($nome);

    print_r($pessoa1);
    ?>
  </pre>
  </body>
</html>
