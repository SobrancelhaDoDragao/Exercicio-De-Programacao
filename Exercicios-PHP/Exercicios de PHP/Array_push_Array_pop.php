<!DOCTYPE html>
<html lang="PT-BR">
  <head>
    <meta charset="utf-8">
    <title>Array_push e Array_pop</title>
  </head>
  <body>
    <pre>
    <?php
    $vetor = array(4,6,7,7);
    print_r($vetor);
    array_push($vetor,'1000');//Array push Serve para colocar um valor na ultima
    //posição, um pouco inutil sendo que o php ja alocar por padrão assim.
    print_r($vetor);
    array_pop($vetor);//Elimina o ultimo valor do array, no caso 100.
    print_r($vetor);
     ?>
   </pre>
  </body>
</html>
