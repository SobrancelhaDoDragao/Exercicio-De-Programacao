<?php
require_once'ClassePessoa.php';

class aluno extends pessoa //Definindo quem é o pai, no caso é ClassePessoa
{
  private $matricula;
  private $curso;

  public function CancelarMatri(){
    echo "Matricula cancelada!";
  }
}

 ?>
