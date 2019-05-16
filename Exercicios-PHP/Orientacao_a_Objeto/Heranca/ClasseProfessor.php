<?php
require_once'ClassePessoa.php';

class professor extends pessoa
{
   private $especialidade;
   private $salario;

   public function ReceberAumento($aumento){
     $this->salario += $aumento;
   }
}

 ?>
