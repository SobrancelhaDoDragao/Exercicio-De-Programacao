<!DOCTYPE html>
<html lang="PT-BR">
  <head>
    <meta charset="utf-8">
    <title>Formulário</title>
    <style>
       div{
         margin: auto;
         width: 500px;
       }
    </style>
  </head>
  <body>
    <fieldset>

    <div>
  <h1>Preencha os campos abaixo:</h1>
  <form action="cadastrando.php" method="POST" enctype="multipart/form-data"><!--O atributo "enctype" deixa o sistema preparado para receber um arquivo-->
    <table>
      <tr>
        <td>Nome do Livro:</td><td><input type="text" name="livro" maxlength="64"></td>
      </tr>
      <tr>
        <td>Nome do Autor:</td><td><input type="text" name="autor" maxlength="64"></td>
      </tr>
      <tr>
        <td>Nome Da Editora:</td><td><input type="text" name="editora" maxlength="64"></td>
      </tr>
      <tr>
        <td>Foto do livro:</td>
        <td><input type="file" name="imagem"</td>
      </tr>
      <tr>
        <td colspan="2" align="center"><input type="reset" value="Apagar"><input type="submit" value="Cadastrar"></td>
      </tr>
    </table>
  </form>
</div>

</fieldset>
  </body>
</html>
