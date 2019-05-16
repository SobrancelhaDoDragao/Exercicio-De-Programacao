<!DOCTYPE html>
<html lang="pt-br">
  <head>
    <meta charset="utf-8">
    <title>Mostrando dados</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <style>
    div{
      margin:auto;
      width: 500px;
      height: 500px;
      font-size: 15pt;
      text-align: center;
    }
    </style>
  </head>
  <body>
  <div>
    <?php
    require_once 'funcoes.php';

    //Chamando a função conectar
    $conexao = conectar();

    //Chamando a função de inserir dados e passando os parâmentros necessários
    inserir($conexao,$_POST['nome'],$_POST['celular'],$_POST['endereco']);

    $sql = $conexao->prepare("select * from contato order by id;");

    $sql->execute();
   ?>

   <!-- Criando o cabeçalho da tabela para exibir os dados, a tabela não foi fechada-->
   <table class="table-bordered table-hover">
     <tr>
       <th class="table-dark">ID</th>
       <th class="table-dark"colspan="6">Nome</th>
       <th class="table-dark">Celular</th>
       <th class="table-dark">Endereço</th>
     </tr>

  <?php

//Muito importante o "fecth" não ser "fecth all", porque assim mostra apenas um
//valor por vez
 while ($exibir = $sql->fetch(PDO::FETCH_ASSOC)){

  //Salvando cada valor retornado em uma variável
  $id = $exibir["id"];
  $nome = $exibir["nome"];
  $celular = $exibir["celular"];
  $endereco = $exibir["endereco"];

//O While ainda não foi fechado
   ?>

   <tr>
     <td><?php echo $id?></td>
     <td colspan="6"><?php echo $nome?></td>
     <td><?php echo $celular?></td>
     <td><?php echo $endereco?></td>
   </tr>

   <?php
   //Finalmente fechando o while
  }
    ?>
  <!-- Fechando a tabela-->
  </table>
<a href="index.php"><button type="button" class="btn btn-primary btn-lg">Inserir mais Dados</button></a>
  </div>
  </body>
</html>
