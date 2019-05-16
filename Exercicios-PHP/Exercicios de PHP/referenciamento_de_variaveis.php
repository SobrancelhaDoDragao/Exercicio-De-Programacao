<!DOCTYPE html>
<html lang="PT-BR" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Apredendo</title>
  </head>
  <body>
    <?php
    $a = 3;
    $b = 3;
    $a = &$b;// Aqui as duas variaveis foram "entrelaçadas".

    $a = 10;
    echo "$a<br>";
    echo "$b";
     ?>
  </body>
</html>
