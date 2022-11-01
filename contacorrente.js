var banco = {
    conta: 'BB',
    saldo: 100,
    tipo: 'Corrente',
    ag: '15800',
}

var valor_saldo = function(){
    console.log('Saldo: ' + banco.saldo);
}
  
var depositar_dinheiro = function(valor){
    banco.saldo = banco.saldo + valor;
}

var sacar_dinheiro = function(valor){
    banco.saldo = banco.saldo - valor;
}

var num_conta = function(){
    console.log('Conta: '+ banco.conta);
}


depositar_dinheiro(50);
sacar_dinheiro(20);
valor_saldo();
num_conta();