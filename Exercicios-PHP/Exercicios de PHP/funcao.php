<!DOCTYPE html>
<html lang="PT-BR">
  <head>
    <meta charset="utf-8">
    <title></title>
    <?php
    function dobro($valor){//função básica
      $dobro = $valor * 2;// Ela pode estar em qualquer lugar, desde que permaneça no mesmo arquivo.
      return $dobro;
    }
     ?>
  </head>
  <body>

    <?php

     $t = 67;
     $resultado = dobro($t);// Salvando o valor retornado pela função.

     echo $resultado;
     echo "<br>Valor original é $t";//A variável original não é modificada, pois seu valor é passado como referência para a variavel temporária da função.

     ?>
  </body>
</html>
