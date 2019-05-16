<?php

class Luta
{
  private $desafiado;
  private $desafiante;
  private $rounds;
  private $aprovado;

       public function MarcarLuta($lutador1,$lutador2){
           if ($lutador1->MostrarCategoria()===$lutador2->MostrarCategoria()){

             if ($lutador1 != $lutador2) {
               echo "<br>Os lutadores possui a mesma categoria, a luta aprovada e marcada:";
               $lutador1->apresentacao();
               $lutador2->apresentacao();
             }
             else {
               echo "Essa luta não pode acontecer, porque um lutador não pode lutar com ele mesmo";
             }
           }
           else {
             echo "<br>Essa luta não pode acontecer, os lutadores não são da mesma categoria";
           }
       }
       public function Lutar(){
         /*Colocar aqui, uma função que retorna uma valor rodômica e esse
         valor vai determinar o vencedor da luta.
         */
       }
}

 ?>
