<?php

 class contas
 {
   private $numero_da_Conta;
   protected $tipo_da_Conta;
   private $dono;
   private $saldo;
   private $status;
//Teste
   //Métodos:
   public function mostrarconta(){
     echo"$this->numero_da_Conta";
   }
   public function __construct(){
     $this ->saldo = 0;
     $this ->status = false;
     echo "<p>Conta criada com sucesso</p>";
   }
   //Métodos para alterar valores dos atributos:
  public function definirNome($nome){
    $this->dono = $nome;
  }
  public function mostrarSaldo(){
    echo "Seu Saldo é ".$this->saldo;
  }
  public function somarSaldo($valor_recebido){
    $this->saldo += $valor_recebido;
  }

  public function subtrairSaldo($valor_tirado){
    $this->saldo = $this->saldo - $valor_tirado;
  }

  public function abrirConta($tipo_da_Conta){
     $this ->status = true;
      if ($tipo_da_Conta == "CC") {
        $this->saldo = 50;
        //Conta Corrente
      }
      if ($tipo_da_Conta == "CP") {
        $this->saldo = 150;
        //Conta Poupança
      }
   }

   public function fecharConta(){
     if ($this->saldo > 0) {
       echo "<p>A conta ainda tem dinheiro não posso fecha-la</p>".$this->saldo;
     }
     else if ($this ->saldo < 0) {
       echo "<p>Não é possível fechar a conta, ela está em débito</p>".$this->saldo;
     }
      else {
        $this ->status = false;
        echo "Conta fechada com sucesso";
      }
   }

   public function depositar($deposito){
     if ($this->status == true) {
         $this->somarSaldo($deposito);
     }
     else {
       echo "<p>Conta fechado não é possível fazer o depósito</p>";
     }
   }

   public function sacar($saque){
     if ($this ->status == true) {
        if ($this->saldo > $saque) {

          $this->saldo = $this->saldo - $saque;
        }
        else {
          echo "<p>Saldo insuficiente para saque</p>";
        }
     }
     else {
       echo "<p>Não posso sacar em um conta que não foi aberta</p>";
     }
   }


   public function pagarMensal(){
     if ($this ->tipo_da_Conta == "CC") {
       $v = 12;
     }
     else if ($this->tipo_da_Conta == "CP") {
       $v = 20;
     }
     if ($this->status == "true") {
       $this->subtrairSaldo($v);
     }
     else {
       echo "<p>Problemas com a conta. Não posso combrar a tarifa<p>";
     }
   }

 }
 ?>
