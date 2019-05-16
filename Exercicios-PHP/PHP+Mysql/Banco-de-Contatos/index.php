<!DOCTYPE html>
<html lang="pt-br">
  <head>
    <meta charset="utf-8">
    <title>Contatos</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <style>
      div{
        margin:auto;
        width: 500px;
        height: 500px;
        font-size: 20pt;
      }
    </style>
  </head>
  <body>
    <div>
      <form action="mostrar_dados.php" method="post">
        <table class="table-bordered table-hover">
          <tr>
            <td colspan="2" class="table-dark"><h1>Contatos do Condomínio</h1></td>
          </tr>
          <tr>
            <td>Nome:</td>
            <td><input type="text" name="nome"></td>
          </tr>
          <tr>
          <td>Celular:</td>
          <td><input type="number"name="celular"></td>
          </tr>
          <tr>
          <td>Endereço:</td>
          <td><input type="text"name="endereco"></td>
          </tr>
          <tr>
            <td colspan="2"style="text-align: center"><input class="btn btn-dark" type="submit"value="Enviar"></td>
          </tr>
        </table>
      </form>
    </div>
  </body>
</html>
