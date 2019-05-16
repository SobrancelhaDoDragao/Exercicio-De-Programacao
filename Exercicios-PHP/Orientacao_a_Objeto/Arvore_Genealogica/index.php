<!DOCTYPE html>
<html lang="PT-BR">
  <head>
    <meta charset="utf-8">
    <title>Instância</title>
  </head>
  <body>
    <?php
     require_once'Abstract-Mother.php';
     require_once'Visitante.php';
     require_once'Aluno.php';
     require_once'alunoBolsista.php';
     //$p1 = new Pessoa; uma classe abstract não pode ser instânciada
     $p1 = new visitante;
     $p2 = new Aluno;
     $p3 = new Bolsista;
     $p3->PagarCurso();//Polimorfismo
    ?>
  </body>
</html>
