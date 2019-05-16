<?php
require_once 'Abstract-Mother.php';

class Aluno extends Pessoa
{
  protected $matricula;
  protected $curso;

  public function PagarCurso(){
    echo "<br>Pagando mensalidade do aluno";
  }
}

?>
