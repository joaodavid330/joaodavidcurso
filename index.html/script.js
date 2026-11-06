const botoes = document.querySelectorAll(".filtros button");
const cartoes = document.querySelectorAll(".cartao");
function filtrar(tipo) {
  cartoes.forEach(function (cartao) {
    const deveMostrar = tipo === "todas" || cartao.classList.contains(tipo);
    cartao.classList.toggle("escondido", !deveMostrar);
  });
  botoes.forEach(function (botao) {
    const ativo = botao.dataset.filtro === tipo;
    botao.classList.toggle("ativo", ativo);
    botao.setAttribute("aria-pressed", ativo);
  });
}
botoes.forEach(function (botao) {
  botao.addEventListener("click", function () {
    filtrar(botao.dataset.filtro);
  });
});