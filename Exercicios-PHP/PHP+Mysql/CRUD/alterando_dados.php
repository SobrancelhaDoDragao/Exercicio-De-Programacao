<?php
//Conectando ao banco
$conexao = new PDO("mysql:dbname=integracao;host=localhost","root","");

//Preparando os dados(Os dois pontos antes dos nomes são importantes)
$stmt = $conexao->prepare("update livros set livro=:livro, autor =:autor, editora = :editora where id = :id;");

//Aparentemente o bindParam só aceita valores dentro de variáveis
$id = 1;
$livro = "Qualidade de Software";
$autor = "André Koscianski";
$editora = "Novatec";

//Refêreciando os dados para cada campo
$stmt->bindParam(":id",$id);
$stmt->bindParam(":livro",$livro);
$stmt->bindParam(":autor",$autor);
$stmt->bindParam(":editora",$editora);

//Executando o comando
$stmt->execute();
 ?>
