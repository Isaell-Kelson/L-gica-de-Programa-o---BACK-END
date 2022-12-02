<?php


require_once 'C:\Users\Isaell\Desktop\LancheDecorator\index.php';
require_once 'C:\Users\Isaell\Desktop\LancheDecorator\FrangoAssado.php';
require_once 'C:\Users\Isaell\Desktop\LancheDecorator\Pao.php';
require_once 'C:\Users\Isaell\Desktop\LancheDecorator\Pepperoni.php';
require_once 'C:\Users\Isaell\Desktop\LancheDecorator\Sanduiche.php';
require_once 'C:\Users\Isaell\Desktop\LancheDecorator\MussarelaRalado.php';




$sanduiche = new Sanduiche();
$sanduiche = new FrangoAssado($sanduiche);
$sanduiche = new Pepperoni($sanduiche);
$sanduiche = new MussarelaRalado($sanduiche);
echo $sanduiche->getNome() . " O preço do seu sanduiche é R$ " . $sanduiche->valor();