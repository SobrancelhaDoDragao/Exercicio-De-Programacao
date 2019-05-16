<!DOCTYPE html>
<html lang="PT-BR">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
 <?php
   $preco = $_GET["p"];
   echo "O preço do produto é R$".number_format($preco,2);
   $preco *= 0.10;
   echo "<br>O preço com desconto é R$".number_format($preco,2);
  ?>
  </body>
</html>
