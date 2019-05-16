<?php
  //Função para inserir dados no banco de dados
  function inserir($conexao,$nome,$celular,$endereco){

    $stmt = $conexao->prepare("insert into contato(nome,celular,endereco)values(:nome,:celular,:endereco);");

    $stmt->bindParam(":nome",$nome);
    $stmt->bindParam(":celular",$celular);
    $stmt->bindParam(":endereco",$endereco);

    $stmt->execute();
  }

 //Função para conectar ao banco de dados
   function conectar(){

    try {
      $conexao = new PDO("mysql:dbname=contatos;host=localhost","root","");
      return $conexao;
   }
   catch (pdoException $e) {
   echo "Erro: ".$e->getMessage();
}
}

?>
