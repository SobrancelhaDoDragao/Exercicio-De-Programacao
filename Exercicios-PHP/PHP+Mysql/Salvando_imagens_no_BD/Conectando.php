<?php
function conectar(){
  $server ='mysql:host=localhost;dbname=integracao';//Resposavel pelo endereciamento
  $usuario ='root';
  $senha = '';

  try {
    $pdo = new pdo($server,$usuario,$senha);
    return $pdo;

  } catch (pdoException $e) {
     echo "Erro: ".$e->getMessage();
  }
}
?>
