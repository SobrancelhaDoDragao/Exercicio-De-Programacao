<?php

class pessoas
{
  public $nome;
  private $idade;

  public function __construct(){//Definindo  a idade para 10.
    $this->idade = 10;
  }

  public function atendente($n){/* Para poder alterar um valor private deve-se criar primeiro uma função publica
    que recebe parâmetros dos novo valores, e nesse ponto, dentro função usado o "this ->", alterar o valor
    com os parâmetros recebidos.Assim toda vez que quiser alterar o valor e só chamar o método(Função). */
    $this-> nome = $n;
  }
  public function mostrar(){
      return $this -> idade;
  }

}

 ?>
