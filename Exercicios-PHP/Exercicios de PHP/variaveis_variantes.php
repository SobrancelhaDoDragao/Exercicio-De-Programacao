<!DOCTYPE html>
<html lang="PT-BR" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <?php
    $x = abc;
    $$x = dfg;// Aqui foi criado uma variavel dentro de outra variavel.

  echo $x;
  echo $$x;
     ?>
  </body>
</html>
