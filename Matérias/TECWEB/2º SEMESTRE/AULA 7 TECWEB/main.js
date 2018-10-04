var n = 5;
switch(n){
    case 1:
        alert('1');
        break;
    case 2:
        alert('2');
        break;
    case 3:
        alert('3');
        break;
    case 4:
        alert('4');
        break;
    default:
        alert('Caso não encontrado');
}

var i;
for(var i=0; i<10; i++){
    alert(i);
}

while(i<5){
    alert(i);
}

// executa antes de verificar
i=0;
do{
    alert(i);
    i++
}while(i<5);


var tituloh1 = document.querySelectorAll('h1');
tituloh1[0].onclick = function(){
    tituloh1[0].textContent = 'Mudei aqui';
}

var tituloh1 = document.querySelectorAll('h1');
tituloh1[1].onclick = function(){
    tituloh1[1].textContent = 'Mudei aqui';
}

var paragrafo = document.getElementById('paragrafo');
alert(paragrafo.textContent);

document.getElementsByTagName();
document.getElementsByClassName();

//document.write("<p>parágrafo aqui </p>");
document.textContent = "<b>Olá</b>, mundo";
document.innerHTML = "<b>Olá</b>, mundo";

var idX = document.getElementById('paragrafo').innerHTML = "Lorem 2";
var idX2 = document.getElementById('imagem').src = "https://img.jovempan.uol.com.br/uploads/2017/09/Temer-Vampiro.jpg";


var idX2 = document.getElementById('imagem');
idX2.onclick = function(){

    if(idX2.src === "https://img.jovempan.uol.com.br/uploads/2017/09/Temer-Vampiro.jpg"){
        idX2.src = "https://abrilveja.files.wordpress.com/2017/09/michel-temer-sindicatos20170912_0003.jpg";
    } else {
        idX2.src = "https://img.jovempan.uol.com.br/uploads/2017/09/Temer-Vampiro.jpg"
    }
}

var x = document.getElementsByClassName("paragrafo1");
x[0].name = "nome1";
x[1].name = "nome2";

var x = document.forms["form1"];
for(var i=0; i<x.length; i++){
    console.log(x.elements[i].value);
}

var estilo = document.getElementById("paragrafo");
estilo.style.background = "black";

var idX2 = document.getElementById('paragrafo2');
//idX2.onMouseOver = function(){
//    idX2.style.background = "Red";
//}

idX2.onMouseOver(idX2.style.background = "Red");