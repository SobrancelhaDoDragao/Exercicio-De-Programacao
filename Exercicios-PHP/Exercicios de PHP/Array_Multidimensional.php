<!DOCTYPE html>
<html lang="PT-BR">
  <head>
    <meta charset="utf-8">
    <title>Array Multidimensional</title>
  </head>
  <body>
    <pre>
    <?php
    echo "Matriz:<br>";
    $vetor1 = array('1','2','3');//array [0]
    $vetor2 = array('4','5','6');// array [1]

    $matriz = array($vetor1,$vetor2);// Matriz criada
    print_r($matriz);
    /*Agora vou alterar o valores dos arrays*/

    $matriz[1][2] = 100;//Aqui vou alterar o valor do 6 para 100.

/* O primeiro vetor corresponde aos arrays primários, e segundo corresponde
aos valores do array escolhido*/

    print_r($matriz);//Mostrando Valores Atualizados(Deu certo).
      ?>
    </pre>
  </body>
</html>
