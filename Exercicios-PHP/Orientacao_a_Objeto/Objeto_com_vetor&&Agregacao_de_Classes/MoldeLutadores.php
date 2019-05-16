<?php

   class DadosLutadores
  {
    private $nome,$nacionalidade,$idade,$altura,$peso,$categoria,$vitorias,$derrotas,$empates;


    public function __construct($nome,$naci,$idade,$altura,$peso,$vitoria,$derrotas,$empates){

   $this->nome = $nome;
   $this->nacionalidade = $naci;
   $this->idade = $idade;
   $this->altura = $altura;
   $this->peso = $peso;
   $this->CategoriaLutador($this->peso);
   $this->vitorias = $vitoria;
   $this->derrotas = $derrotas;
   $this->empates = $empates;
   }

      //Métodos
      public function MostrarCategoria(){
        return $this->categoria;
      }

     //Métodos Especiais
      public function CategoriaLutador($peso){

       if ($this->peso<52.2){
        $this->categoria = 'Invalido';
      }
      elseif ($this->peso<=70.0) {
        $this->categoria = 'leve';
      }
      elseif ($this->peso<=83.9) {
        $this->categoria = 'medio';
      }
      elseif ($this->peso<=120.2) {
       $this->categoria = 'pesado';
      }
     else {
      $this->categoria = 'Invalido';
     }
  }

      public function apresentacao(){

      echo "<p>--------------------------------------------------------------------------------------------------------</p>";
      echo "<p>CHEGOU A HORA! O LUTADOR</p> ".$this->nome;
      echo " Veio diretamente de ".$this->nacionalidade;
      echo " tem ".$this->idade ." anos e pesa ".$this->peso ," kilos ";
      echo "<br>Ele tem ".$this->vitorias." vitorias, ";
      echo $this->derrotas." derrotas e ".$this->empates." empates";

      }

      public function status(){

        echo "<p>-----------------------------------------------------------------------------------------------------</p>";
        echo "<p>".$this->nome." é um peso ".$this->categoria;
        echo " e já ganhou ".$this->vitorias." vezes ";
        echo " perdeu ".$this->derrotas." vezes e ";
        echo " empatou ".$this->empates." vezes!";
      }
   }
 ?>
