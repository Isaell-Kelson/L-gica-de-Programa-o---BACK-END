<?php

require_once 'C:\Users\Isaell\Desktop\LancheDecorator\pao.php';
require_once 'C:\Users\Isaell\Desktop\LancheDecorator\Decorator.php';

class FrangoAssado extends Decorator
{
    private $pao;

    public function __construct(Pao $pao) 
    {
        $this->pao = $pao;   
    }

    public function getNome()
    {
        return $this->pao->getNome(). ", Frango assado";
    }

    public function valor()
    {
        return 4.50 + $this->pao->valor();
    }
}