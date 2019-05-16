<!DOCTYPE html>
<html lang="pt-br">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <pre>
    <?php
    //Conexão com o banco de dados.
    $conexao = new PDO("mysql:dbname=cadastro;host=localhost","root","");

    //Mandando o comando para o banco de dados.
    $stmt = $conexao->prepare("select * from gafanhotos order by nome;");

    //Executando o comando.
    $stmt->execute();

    //Preparando os dados para mostrar.
    $resultado = $stmt->fetchALL(PDO::FETCH_ASSOC);

    //Mostrando todos os dados da tabela como o comando adequado.
    print_r($resultado);
    ?>
  </pre>
  </body>
</html>
