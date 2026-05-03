var activePage = window.location.pathname;
let nav_home = document.getElementById("nav_home");
let nav_sobre = document.getElementById("nav_sobre");
let nav_formacao = document.getElementById("nav_formacao");
let nav_projetos = document.getElementById("nav_projetos");

if (activePage.endsWith("/") || activePage.includes("index.html")) {
  nav_home.classList.add("active");
}

if (activePage.includes("sobre_mim.html")) {
  nav_sobre.classList.add("active");
}

if (activePage.includes("formacao.html")) {
  nav_formacao.classList.add("active");
}

if (activePage.includes("projetos.html")) {
  nav_projetos.classList.add("active");
}

let hamburguer = document.querySelector(".navbar_hamburguer");
let menu = document.querySelector(".navbar_menu");

hamburguer.onclick = function () {
  menu.style.display = "flex";
  menu.classList.toggle("showing");

  if (!menu.classList.contains("showing")) {
    menu.style.display = "none";
  }
};

document.querySelector(".botao_top").addEventListener("click", function () {
  window.scrollTo(0, 0);
});
