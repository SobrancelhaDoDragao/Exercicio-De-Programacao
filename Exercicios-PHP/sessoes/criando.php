<?php
/*Sessão é um array criado no navegador, que guarda vários valores que pode ser
acessados através de qualquer arquivo*/

//Inciando a sessão
session_start();

//As seções são arrays
$_SESSION["idade"] = 20;
$_SESSION["nome"] = "Eudson";
$_SESSION["id"] = session_id();
echo $_SESSION['id'];
 ?>
