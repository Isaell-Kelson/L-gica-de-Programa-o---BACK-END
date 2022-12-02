<?php

require_once 'C:\Users\Isaell\Desktop\LancheDecorator\pao.php';

class Pepperoni extends Decorator
{
    private $pao;
    
    public function __construct(Pao $pao) 
    {
        $this->pao = $pao;   
    }

    public function getNome()
    {
        return $this->pao->getNome(). ", Pepperoni";
    }

    public function valor()
    {
        return 0.99 + $this->pao->valor();
    }
}