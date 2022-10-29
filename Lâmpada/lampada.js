const turnOn = document.getElementById ( 'ligado' );
const turnOff = document.getElementById ( 'desligado' );

function lampOn () {
    lamp.src = './img/alumiou.png';
    
}

function lampOff () {
    lamp.src = './img/apagada.png';
    
}

turnOn.addEventListener ( 'click', lampOn );
turnOff.addEventListener ( 'click', lampOff );