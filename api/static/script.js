// Deixar página ativa em azul no Navbar

var activePage = window.location.pathname;
let nav_home = document.getElementById("nav_home");
let nav_servicos = document.getElementById("nav_servicos");
let nav_sobre = document.getElementById("nav_sobre");
let nav_formacao = document.getElementById("nav_formacao");
let nav_projetos = document.getElementById("nav_projetos");

if (activePage == "/") {
  nav_home.classList.toggle("active");
}

if (activePage == "/servicos") {
    nav_servicos.classList.toggle("active");
  }

if (activePage == "/sobre_mim") {
  nav_sobre.classList.toggle("active");
}

if (activePage == "/formacao") {
  nav_formacao.classList.toggle("active");
}

if (activePage == "/projetos") {
    nav_projetos.classList.toggle("active");
}




// Funcionalidade Menu Hamburguer

// Pegar o menu de hamburguer e as opções do menu
hamburguer = document.querySelector(".navbar_hamburguer");
menu = document.querySelector(".navbar_menu");

// Quando clicar no menu de hamburguer, ganhará uma classe chamada "showing", 
// e enquanto o menu de hamburguer ter essa classe as opções aparecerão
// Se clicar denovo (para fechar), fecha as opções do menu e tira a classe "showing" do menu de hamburguer.
hamburguer.onclick = function() {
  menu.style.display = "flex";
  menu.classList.toggle("showing");
  if (menu.classList.contains("showing")) {
    menu.style.display = "none";
  }

}

document.querySelector(".botao_top").addEventListener("click", function() {
  window.scrollTo(0, 0);
});
