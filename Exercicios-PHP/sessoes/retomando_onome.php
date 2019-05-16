<?php
session_start();

echo "O usuário ".$_SESSION['nome'];
echo " Tem ".$_SESSION['idade']." anos ";
echo " e seu id de sessão é ".session_id()."<br>";

 ?>
