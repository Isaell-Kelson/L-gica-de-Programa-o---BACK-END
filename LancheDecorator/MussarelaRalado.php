<?php

require_once 'C:\Users\Isaell\Desktop\LancheDecorator\Sanduiche.php';

class MussarelaRalado extends Decorator
{
    private $pao;
    
    public function __construct(Pao $pao) 
    {
        $this->pao = $pao;   
    }

    public function getNome()
    {
        return $this->pao->getNome(). ", Mussarela ralado";
    }

    public function valor()
    {
        return 2 + $this->pao->valor();
    }
}