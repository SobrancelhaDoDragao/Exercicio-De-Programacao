<!DOCTYPE html>
<html lang="PT-BR">
  <head>
    <meta charset="utf-8">
    <title>Objetos com vetores</title>
  </head>
  <body>

    <?php
    require_once"MoldeLutadores.php";
    require_once"Molde_Luta.php";
    //Criando um vetor para armazenar o lutadores
    $lutadores = array();
    //Primeiro lutador cadastrado
    $lutadores[0] = new DadosLutadores("Pretty Boy","França",31,1.75,68.5,11,2,1);
    //Segundo lutador cadastrado
    $lutadores[1] = new DadosLutadores("Putscript","Brasil",29,1.68,57.8,14,2,3);
    //Interação entre dois Objetos:
    $Luta = new Luta();
    $Luta->MarcarLuta($lutadores[0],$lutadores[1]);
     ?>

  </body>
</html>
