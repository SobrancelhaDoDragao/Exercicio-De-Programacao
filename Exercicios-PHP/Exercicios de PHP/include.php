<!DOCTYPE html>
<html lang="PT-BR" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <?php
    $x = 10;
    echo "Aqui vou chamar um função de outro documento para altera o valor de $x";
    include'funcao.php';
    $salvar = dobro($x);

    echo "$salvar";// Era pra colocar um ponteiro na função mas, não quis alterar outro arquivo.
//bugo
     ?>
  </body>
</html>
