<?php
require_once 'conexao.php';
class Usuario extends Conexao{

  private $id;
  private $nome;
  private $idade;
  private $sexo;
  private $telefone;
  private $email;

  public function mostrarnome(){
    return $this->nome;
  }
  public function alterarnome($alteracao){
    $this->nome = $alteracao;
  }

  public function mostraridade(){
    return $this->idade;
  }
  public function alteraridade($alteracao){
    $this->idade = $alteracao;
  }

  public function mostrarsexo(){
    return $this->sexo;
  }
  public function alterarsexo($alteracao){
    $this->sexo = $alteracao;
  }

  public function mostrartelefone(){
    return $this->telefone;
  }
  public function alterartelefone($alteracao){
    $this->telefone = $alteracao;
  }

  public function mostraremail(){
    return $this->email;
  }
  public function alteraremail($alteracao){
    $this->email = $alteracao;
  }
  //Inserir dados
  public function inserir($nome,$idade,$sexo,$telefone,$email){

    $stmt = $this->conexao->prepare("insert into usuario(nome,idade,sexo,telefone,email)values(:nome,:idade,:sexo,:telefone,:email);");

    $stmt->bindParam(":nome",$nome);
    $stmt->bindParam(":idade",$idade);
    $stmt->bindParam(":sexo",$sexo);
    $stmt->bindParam(":telefone",$telefone);
    $stmt->bindParam(":email",$email);

    $stmt->execute();
  }
}
?>
