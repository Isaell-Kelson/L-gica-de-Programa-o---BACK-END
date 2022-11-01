function main()
{
 var resp = document.getElementById('resp');
 var n1 = parseFloat(document.getElementById("n1").value);
 var n2 = parseFloat(document.getElementById("n2").value);
 var resultado='';

 if(document.getElementById('soma').checked)
  resultado = soma(n1, n2);
 if(document.getElementById('subtracao').checked)
  resultado = subtracao(n1, n2);
 if(document.getElementById('multiplicacao').checked)
  resultado = multiplicacao(n1, n2);
 if(document.getElementById('divisao').checked)
  resultado = divisao(n1, n2);

}

function soma(x, y)
{
  
  return (x+y);
}

function subtracao(x, y)
{
  
  return (x-y);
}

function multiplicacao(x, y)
{
  
  return (x*y);
}

function divisao(x, y)
{
  
  return (x/y);
}