<?php

abstract class Pessoa
{
  protected $nome;
  protected $idade;
  protected $sexo;

  public final function fazerAniversario(){//Esse método não pode ser sobrescrito pelas
    $this->idade++;                        //classe filhas devido a esse "final".
  }

}
?>
