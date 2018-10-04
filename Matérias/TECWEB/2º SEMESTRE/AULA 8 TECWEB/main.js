var imagem = document.querySelectorAll('img');

imagem[0].onclick = function(){
    var meulocal = imagem[0].getAttribute('src');
    if (meulocal === 'imagens/troll.jpg') {
            imagem[0].setAttribute('src', 'imagens/homer1.gif')
    } else {
            imagem[0].setAttribute('src', 'imagens/troll.jpg')
    } 
}

imagem[1].onclick = function(){
        var meulocal = imagem[1].getAttribute('src');
        if (meulocal === 'imagens/Troll+Face.jpg') {
                imagem[1].setAttribute('src', 'imagens/homer2.gif')
        } else {
                imagem[1].setAttribute('src', 'imagens/Troll+Face.jpg')
        } 
}

var titulo = document.querySelector('h1');
var botao = document.querySelector('button');

function mudaNomeUsuario(){

        var meuNome = prompt('Insira seu nome');
        localStorage.setItem('nome', meuNome);
        titulo.innerHTML = "Bem vindo(a) a minha <i>página pessoal, </i>" +meuNome;

        localStorage.removeItem('nome');
}

if (!localStorage.getItem('nome')) {
        mudaNomeUsuario();
} else {
        var nomeArmazenado = localStorage.getItem('nome');
        titulo.innerHTML = "Bem vindo(a) a minha <i>página pessoal, </i>" +nomeArmazenado;
}

botao.onclick = function(){
        mudaNomeUsuario();
}