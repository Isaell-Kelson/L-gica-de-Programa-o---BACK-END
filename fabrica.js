const pc = {
    produto1: 'PC',
    ram: 8,
    hd: 500,
    cpu: 3.2,

}

const server = {
    produto2: 'Server',
    ram2: 4,
    hd2: 250,
    cpu2:4.0,

}

function criarPC(produto1, ram, hd, cpu){
    return{
        produto1,
        ram,
        hd,
        cpu,
    }
}

function criarServer(produto2, ram2, hd2, cpu2){
    return{
        produto2,
        ram2,
        hd2,
        cpu2,
    }
}


const pc1 = criarPC('PC', 8, 500, 3.2);
console.log(pc1);

const server1 = criarPC('Server', 4, 250,4.0);
console.log(server1);