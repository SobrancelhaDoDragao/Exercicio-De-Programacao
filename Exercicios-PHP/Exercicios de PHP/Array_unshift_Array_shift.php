<!DOCTYPE html>
<html lang="PR-BR">
  <head>
    <meta charset="utf-8">
    <title>Array_shift e Array_unshift</title>
  </head>
  <body>
    <pre>
    <?php
    $vetor = array(5,6,7,2);
    array_unshift($vetor,'1000');//Adcionando o valor '1000' na primeira posição
    print_r($vetor);
    array_shift($vetor);//Removendo o primeiro valor do vetor
    print_r($vetor);
     ?>
   </pre>
  </body>
</html>
