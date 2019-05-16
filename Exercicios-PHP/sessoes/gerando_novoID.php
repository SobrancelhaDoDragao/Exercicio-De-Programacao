<!DOCTYPE html>
<html lang="pt-br">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <pre>
    <?php
    //Para gerar é obrigatório dar include no arquivo que criou a sessão
    require_once 'criando.php';

    //Gerando um novo ID
    session_regenerate_id();
    echo session_id();

    //Mostrando todos os valores guardados nas sessão
    print_r($_SESSION);
     ?>
     </pre>
  </body>
</html>
