<!DOCTYPE html>
<html lang="PT-BR">
  <head>
    <meta charset="utf-8">
    <title>Data de hoje</title>

    <style >
      div{
        margin:auto;
        width: 700px;

      }
      fieldset{
        text-align: center;
        background:#40a459;
      }
      fieldset.interno{
        margin: auto;
        width: 50px;
        background:#9de71f;
      }
    </style>
  </head>
  <body>
    <div>
    <fieldset><legend>Data e hora</legend>
      <fieldset class="interno">
  <?php

   $data = date('d/n/y');
   $hora = date('G:i');
   echo $data;
   echo "<br>$hora";
   ?>
 </fieldset>
 </fieldset>
</div>
  </body>
</html>
