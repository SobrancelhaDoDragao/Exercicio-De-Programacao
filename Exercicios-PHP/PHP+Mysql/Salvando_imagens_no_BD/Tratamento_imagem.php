<?php
function imagem(){

  conectar();
  /*A variável global "$_File" salva o arquivo em uma pasta temporâria dentro do sistema do PHP*/
  if (isset($_FILES['imagem'])) {

    //Arrumando a extensão do arquivo.
    $extensao = strtolower(substr($_FILES['imagem']['name'],-4));

    //Criando um novo nome para o arquivo.
    $novo_nome = md5(time()).$extensao;

    //Mostrando caminho que vai ser seguido para armazenar o arquivo.
    $pasta_de_imagens = "upload/";

    //Essa função acessa a pasta de arquivos do php, e salva o arquivo escolhido na pasta "upload" no computador.
    move_uploaded_file($_FILES['imagem']['tmp_name'],$pasta_de_imagens.$novo_nome);

    //Retornando o nome do arquivo para que ele seja salvo no Banco de dados.
    return $pasta_de_imagens.$novo_nome;
  }
  else {
    echo "Nenhum arquivo foi carregado";
  }
}
 ?>
