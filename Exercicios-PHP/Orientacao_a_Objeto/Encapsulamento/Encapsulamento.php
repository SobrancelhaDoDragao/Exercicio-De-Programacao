<!DOCTYPE html>
<html lang="PT-BR">
  <head>
    <meta charset="utf-8">
    <title>Encapsulamento</title>
  </head>
  <body>
    <pre>
    <?php
      require_once 'Classes.php';

      $pedido1 = new cachorros;
      $pedido2 = new cachorros;
      $pedido1->pedido('tadeu','pinter',1);
      $pedido2->pedido('Eudson','Pastor Alemã0',3);

     ?>
   </pre>
  </body>
</html>
