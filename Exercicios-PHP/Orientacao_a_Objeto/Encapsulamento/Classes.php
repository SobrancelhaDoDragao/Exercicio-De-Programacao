<?php
//PET-SHOP
/*Essa classe vai servir para salvar dados dos cachorro coletados no atendimento, e
também o pedido do cliente.*/
require_once 'interface.php';
class cachorros implements pedido
{
   private $dono_nome;
   private  $raca;
   private $pedido;

   //Métodos
  private function Executar_pedido($cliente_nome,$raca_dog,$pedido_cliente){
     $this->dono_nome = $cliente_nome;
     $this->raca = $raca_dog;
     $this->pedido = $pedido_cliente;

     switch ($this->pedido) {

       case 1:
         //Completo
         echo "O cachorro do cliente: $this->dono_nome esta limpo e tosado<br>";
         break;
       case 2:
        //Só banho
         echo "O cachorro do cliente: $this->dono_nome está limpo<br>";
         break;
       case 3:
       //Só tosa
         echo "O cachorro do cliente: $this->dono_nome esta tosado<br>";
         break;
       default:
         echo "Ocorreu algum erro no código";
         break;
     }
   }

   public function pedido($cliente_nome,$raca_dog,$pedido_cliente){
     $this->Executar_pedido($cliente_nome,$raca_dog,$pedido_cliente);
     /*Isso não faz sentido a ideia era deixar tudo nesse arquivo privado
     mas no final de tudo teve que criar um função public aqui dentro, pra que serve
     o impementes então? A ideia inicial dele não era ser uma forma de acesso este documento?
     Era mais facil e simples, chamar diretamenta essa função publica aqui dentro*/

     //Em suma: implementes é desnecessário
   }
}
 ?>
