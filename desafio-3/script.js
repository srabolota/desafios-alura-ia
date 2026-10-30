/* ==========================================================
   LÓGICA E INTERATIVIDADE (JAVASCRIPT) - LISTA DE TAREFAS
   O JavaScript controla o comportamento da página (o que acontece quando clicamos).
   ========================================================== */

// 1. CAPTURANDO ELEMENTOS DO HTML
// Usamos getElementById para 'pegar' os elementos da página pelo ID deles
const inputTarefa = document.getElementById("input-tarefa");
const btnAdicionar = document.getElementById("btn-adicionar");
const listaTarefas = document.getElementById("lista-tarefas");
const mensagemVazia = document.getElementById("mensagem-vazia");

// 2. CONFIGURANDO OS EVENTOS (OUVINTES DE AÇÃO)
// Quando o usuário clica no botão "Adicionar":
btnAdicionar.addEventListener("click", adicionarTarefa);

// Quando o usuário pressiona uma tecla no campo de texto:
inputTarefa.addEventListener("keypress", function (evento) {
  // Se a tecla pressionada for 'Enter', adiciona a tarefa sem precisar clicar no botão
  if (evento.key === "Enter") {
    adicionarTarefa();
  }
});

// Ao abrir a página pela primeira vez, carrega as tarefas salvas anteriormente
window.addEventListener("DOMContentLoaded", carregarTarefas);

// 3. FUNÇÃO PRINCIPAL: ADICIONAR NOVA TAREFA
function adicionarTarefa() {
  const texto = inputTarefa.value.trim(); // .trim() remove espaços vazios no início e fim

  // Validação: não permitir adicionar tarefas em branco
  if (texto === "") {
    alert("Por favor, digite o nome de uma tarefa!");
    return;
  }

  // Cria o elemento visual da tarefa na lista
  criarElementoTarefa(texto, false);

  // Limpa o campo de texto e coloca o cursor de volta nele
  inputTarefa.value = "";
  inputTarefa.focus();

  // Salva no armazenamento do navegador e atualiza mensagem
  salvarTarefas();
  atualizarVisibilidadeMensagem();
}

// 4. FUNÇÃO AUXILIAR: CRIAR O ELEMENTO HTML DE UMA TAREFA
function criarElementoTarefa(texto, concluida = false) {
  // Cria o item da lista <li>
  const li = document.createElement("li");
  li.classList.add("item-tarefa");
  if (concluida) {
    li.classList.add("concluida");
  }

  // Cria a área do texto
  const spanTexto = document.createElement("span");
  spanTexto.classList.add("texto-tarefa");
  spanTexto.textContent = texto;

  // Permitir marcar como concluída também ao clicar no próprio texto
  spanTexto.addEventListener("click", () => alternarConclusao(li));

  // Cria o container para os botões de ação
  const divAcoes = document.createElement("div");
  divAcoes.classList.add("acoes-tarefa");

  // Botão 1: Concluir (marca/desmarca)
  const btnConcluir = document.createElement("button");
  btnConcluir.textContent = concluida ? "Desfazer" : "Concluir";
  btnConcluir.classList.add("btn", "btn-acao", "btn-concluir");
  btnConcluir.addEventListener("click", () => alternarConclusao(li, btnConcluir));

  // Botão 2: Remover (exclui a tarefa)
  const btnRemover = document.createElement("button");
  btnRemover.textContent = "Remover";
  btnRemover.classList.add("btn", "btn-acao", "btn-remover");
  btnRemover.addEventListener("click", () => removerTarefa(li));

  // Montando a estrutura: coloca botões no div, e texto + div dentro do <li>
  divAcoes.appendChild(btnConcluir);
  divAcoes.appendChild(btnRemover);
  li.appendChild(spanTexto);
  li.appendChild(divAcoes);

  // Adiciona o novo item dentro da lista <ul>
  listaTarefas.appendChild(li);
}

// 5. FUNÇÃO: CONCLUIR / DESFAZER TAREFA
function alternarConclusao(itemElemento, botaoConcluir = null) {
  // Alterna a classe 'concluida' (se tem, tira; se não tem, põe)
  itemElemento.classList.toggle("concluida");

  // Se o botão foi passado, atualiza o texto dele
  if (!botaoConcluir) {
    botaoConcluir = itemElemento.querySelector(".btn-concluir");
  }

  if (itemElemento.classList.contains("concluida")) {
    botaoConcluir.textContent = "Desfazer";
  } else {
    botaoConcluir.textContent = "Concluir";
  }

  salvarTarefas();
}

// 6. FUNÇÃO: REMOVER TAREFA
function removerTarefa(itemElemento) {
  // Remove o elemento da tela
  itemElemento.remove();

  // Atualiza os dados salvos e a mensagem da lista vazia
  salvarTarefas();
  atualizarVisibilidadeMensagem();
}

// 7. FUNÇÃO: ATUALIZAR MENSAGEM DE LISTA VAZIA
function atualizarVisibilidadeMensagem() {
  const quantidadeTarefas = listaTarefas.children.length;
  if (quantidadeTarefas === 0) {
    mensagemVazia.style.display = "block";
  } else {
    mensagemVazia.style.display = "none";
  }
}

// 8. BÔNUS DIDÁTICO: SALVAR NO NAVEGADOR (localStorage)
// Isso garante que suas tarefas não sumam quando a página for recarregada!
function salvarTarefas() {
  const tarefas = [];
  const itens = listaTarefas.querySelectorAll(".item-tarefa");

  itens.forEach((item) => {
    tarefas.push({
      texto: item.querySelector(".texto-tarefa").textContent,
      concluida: item.classList.contains("concluida"),
    });
  });

  // Salva o array convertido em texto JSON
  localStorage.setItem("minhas_tarefas", JSON.stringify(tarefas));
}

function carregarTarefas() {
  const dados = localStorage.getItem("minhas_tarefas");
  if (dados) {
    const tarefas = JSON.parse(dados);
    tarefas.forEach((tarefa) => {
      criarElementoTarefa(tarefa.texto, tarefa.concluida);
    });
  }
  atualizarVisibilidadeMensagem();
}
