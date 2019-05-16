<!DOCTYPE html>
<html lang="PT-BR">
  <head>
    <meta charset="utf-8">
    <title>Dia da Escola</title>
    <style>
      h1{
        text-align: center;
      }
      fieldset{
        width: 700px;
        margin:auto;
        border-color: black;
      }
    </style>
  </head>
  <body style="background-color:#e3ef1d">

    <fieldset>
    <?php
     $dia = date('D');

     switch ($dia) {
        case 'Mon':
         echo "<h1>Hoje é segunda portanto, tem aula!</h1>";
         break;
        case 'Tue':
         echo "<h1>Hoje é terça portanto, tem aula!</h1>";
        break;
        case 'Wed':
          echo "<h1>Hoje é quarta portanto, tem aula!</h1>";
          break;
        case 'thu':
          echo "<h1>Hoje é quinta portanto, tem aula!</h2>";
          break;
        case 'Fri':
            echo "<h1>Hoje é sexta portanto, tem aula!</h2>";
            break;
        case 'Sat':
          echo "<h1>Hoje é sabado portanto, não tem aula!</h2>";
          break;
        case 'Sun':
          echo "<h1>Hoje é domingo portanto, não tem aula!</h2>";
          break;
       default:
         echo "Erro";
         break;
     }

     ?>
   </fieldset>
  </body>
</html>
