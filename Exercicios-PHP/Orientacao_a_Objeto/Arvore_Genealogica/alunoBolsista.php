<?php

 class Bolsista extends Aluno //Essa classe é neta da classe mãe.
 {
   public function PagarCurso(){
     echo "<br> Esse aluno é bolsista ele paga apenas 50% do curso";//Aqui estou sobrepondo o método da classe mãe aluno.
   }
 }

?>
