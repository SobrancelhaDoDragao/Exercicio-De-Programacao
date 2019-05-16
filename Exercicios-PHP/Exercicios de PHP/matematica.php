<!DOCTYPE html>
<html lang="PT-BR">
  <head>
    <meta charset="utf-8">
    <title>Matematica no PHP</title>
    <style>
      h1{
        text-align: center;
        color:#25eb0a;
      }
    </style>
  </head>
  <body>
    <?php
    $numero1 = 5;
    $numero2 = 5;
    $soma = $numero1 + $numero2;// salvado o resultado da operação

    echo "<h1>$soma</h1>";
    echo "<h1>o valor é </h1>".($numero1-$numero2);//Forma mais prática de fazer a conta.
     ?>
  </body>
</html>
