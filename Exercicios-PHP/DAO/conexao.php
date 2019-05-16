<?php
//Sql é uma classe filha da classe nativa do PHP: PDO
abstract class Conexao extends PDO{

  //So classes filha podem acessar essa variável
  protected  $conexao;

  //Quando essa classe for instânciada automaticamente vai ser conectada ao banco.
  public function __construct(){
     try {
       $this->conexao = new PDO("mysql:dbname=DAO;host=localhost","root","");
       return $this->conexao;
    }
    catch (pdoException $e) {
    echo "Erro: ".$e->getMessage();
   }
}
}
?>
