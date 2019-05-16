<!DOCTYPE html>
<html lang="PT-BR">
  <head>
    <meta charset="utf-8">
    <title>Testando</title>
  </head>
  <body>
    <?php
    $nome = "         Eudson Durães Silva  ";//Criando a variável.
    echo "$nome";
    $tamanho = strlen($nome);//Medindo o tamanho da variável com espaços.
    echo "$tamanho";//Mostrando o tamanho.
    $nome = trim($nome);//Retirando os espaços vazios.
    $tamanho = strlen($nome);//Tamanha após a redução.
    echo "<BR>$tamanho";//Mostrando o novo tamanho.
     ?>
  </body>
</html>
