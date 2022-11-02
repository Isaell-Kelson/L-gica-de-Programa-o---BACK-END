var celular = {
    cor: "Azul",
    altura: "20cm",
    largura: "7cm",
}

var especificacoes = function(){
    console.log('Especificações: ' + celular.cor, celular.altura, celular.largura);
}


var produto = ['Novo', ' Importado', ' PTbr',];

var detalhe = function(){
    console.log('Detalhes: ' + produto);
}


especificacoes();
detalhe();