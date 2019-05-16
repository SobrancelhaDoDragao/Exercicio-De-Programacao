<!DOCTYPE html>
<html lang="PT-BR">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <pre>
    <?php
     require_once 'ClassePessoa.php';
     require_once 'ClasseAluno.php';
     require_once 'ClasseProfessor.php';
     require_once 'ClasseFuncionario.php';

    $p1 = new pessoa();
    $p2 = new aluno();
    $p3 = new professor();
    $p4 = new funcionario();

    $p1->DefinirNome("A Grande Mãe");//Esse método é defino somente na classe mãe
    $p1->DefinirIdade(57);
    $p1->DefinirSexo("Feminino");
    $p1->MostrarNome();

    $p2->DefinirNome("Pedro");//Mas todas as classe tem direito a esse método
    $p2->DefinirIdade(14);
    $p2->DefinirSexo("Masculino");
    $p2->MostrarNome();

    $p3->DefinirNome("Vitor");
    $p3->DefinirIdade(26);
    $p3->DefinirSexo("Masculino");
    $p3->MostrarNome();

    $p4->DefinirNome("Joaquin");
    $p4->DefinirIdade(45);
    $p4->DefinirSexo("Masculino");
    $p4->MostrarNome();

    print_r($p1);
    print_r($p2);
    print_r($p3);
    print_r($p4);
     ?>
   </pre>
  </body>
</html>
