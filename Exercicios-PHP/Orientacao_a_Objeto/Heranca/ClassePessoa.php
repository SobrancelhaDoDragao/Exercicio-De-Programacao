<?php

  class pessoa
  {
    private $nome;
    private $idade;
    private $sexo;

    public function FazerAniver(){//Todas as classe filhas terão o direito de usar
      $this->idade++;             //esses métodos.
    }
    public function DefinirNome($nome){
      $this->nome = $nome;
    }
    public function DefinirIdade($idad){
      $this->idade = $idad;
    }
    public function DefinirSexo($sex){
      $this->sexo = $sex;
    }
    public function MostrarNome(){
      echo "<br>".$this->nome;
    }
  }

 ?>
