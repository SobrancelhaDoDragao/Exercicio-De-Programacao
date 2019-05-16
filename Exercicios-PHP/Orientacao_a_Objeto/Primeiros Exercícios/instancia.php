<!DOCTYPE html>
<html lang="PT-BR">
  <head>
    <meta charset="utf-8">
    <title>Intânciado Objetos</title>
  </head>
  <body>
    <pre>
    <?php
     require_once 'Pessoas.php';

     $pessoas  = new pessoas;
     $pessoas -> nome = 'eudson';//Acessando de maneira convecional um atributo público.
     print_r($pessoas);
     $pessoas -> atendente('Joaquin');//Aqui usando o método SET.
      print_r($pessoas);
     ?>
   </pre>
  </body>
</html>
