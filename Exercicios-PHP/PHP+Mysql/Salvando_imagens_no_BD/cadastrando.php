<!DOCTYPE html>
<html lang="PT-BR">
  <head>
    <meta charset="utf-8">
    <title>Envio de Dados</title>
    <style>
      h1{
        text-align: center;
        color: rgb(94, 152, 237);
      }
    </style>
  </head>
  <body>
    <a href="index.php"><input type="button"value="Voltar" <br> </a>
    <?php
    include'Conectando.php';
    include'Tratamento_imagem.php';
    $conexao = conectar();
    $endereco_imagem = imagem();//A imagem está funcionando
    $sql = 'insert into livros(livro,autor,editora,imagem) values(?,?,?,?)';
    $stmt = $conexao->prepare($sql);
    $stmt->bindValue(1,$_POST['livro']);
    $stmt->bindValue(2,$_POST['autor']);
    $stmt->bindValue(3,$_POST['editora']);
    $stmt->bindValue(4,$endereco_imagem);
    if ($stmt->execute()) {
      echo "Dados salvos com sucesso!";
    }
    else {
      echo "Erro ao salvar!";
    }
     ?>
  </body>
</html>
