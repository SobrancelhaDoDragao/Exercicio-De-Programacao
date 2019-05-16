<?php
//Conectando ao banco
$conexao = new PDO("mysql:dbname=integracao;host=localhost","root","");

//Preparando o comando
$stmt = $conexao->prepare("delete from livros where id = :id");

//Definindo quem vai ser excluindo
$id = 2;

//Referênciando campos
$stmt->bindParam(":id",$id);

//Executando comando
$stmt->execute();
 ?>
