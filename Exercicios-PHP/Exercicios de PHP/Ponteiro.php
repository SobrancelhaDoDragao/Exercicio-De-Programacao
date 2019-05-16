<!DOCTYPE html>
<html lang="PT-BR">
  <head>
    <meta charset="utf-8">
    <title>Ponteiro no PHP</title>
  </head>
  <body>
    <?php
     function mudanca(&$ponteiro){//Passando o endereço da variável $y como referência.
       $ponteiro = 0;
       /*Aqui eu alterei o valor da variável original através de um ponteiro
       dentro da função, um bom geito de cotornar o problema das variáveis
       locais temporárias, sem usar return*/
     }
     $y = 10;
     echo "$y";
     mudanca($y);
     echo "<br>$y";
     ?>
  </body>
</html>
