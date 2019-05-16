<!DOCTYPE html>
<html lang="PT-BR">
  <head>
    <meta charset="utf-8">
    <title>Função Soma</title>
  </head>
  <body>
    <?php
     function soma($v){
       $v = func_get_args();
       $total = func_num_args();
       $s = 0;
/* A função func_get_args cria o tanto de variáveis necessárias e o $total conta
a quantidade da variáveis recebidas e o for soma todos os valores e guarda na
variável $s*/
       for ($i=0; $i < $total ; $i++) {
          $s += $v[$i];
       }
       echo "$s";
     }
     soma(5,7,8,9);
     ?>
  </body>
</html>
