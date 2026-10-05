// Elementos da página utilizados pelo JavaScript
const form = document.getElementById("form-busca");
const tipo = document.getElementById("tipo-busca");
const termo = document.getElementById("termo");
const lista = document.getElementById("lista-resultados");

// Guarda a busca atual e a página em que o usuário está
let buscaAtual = "";
let paginaAtual = 1;


/* Realiza a busca escolhida pelo usuário */

form.addEventListener("submit", function(evento) {

    // Impede o formulário de recarregar a página
    evento.preventDefault();

    // Verifica qual tipo de busca foi selecionado
    if (tipo.value === "videos") {

        // Guarda o termo pesquisado e inicia pela primeira página
        buscaAtual = termo.value;
        paginaAtual = 1;

        buscarVideos();

    } else if (tipo.value === "empresas") {

        buscarEmpresas();

    } else {

        // Busca uma empresa diretamente pelo seu ID
        mostrarEmpresa(termo.value);
    }
});


/* ---------- Busca de vídeos ---------- */

async function buscarVideos() {

    // Faz uma requisição para a rota de vídeos da API
    const resposta = await fetch(
        `/videos/${encodeURIComponent(buscaAtual)}/${paginaAtual}`
    );

    // Converte a resposta JSON da API para um objeto JavaScript
    const videos = await resposta.json();

    // Limpa os resultados anteriores
    lista.innerHTML = "";

    // Verifica se nenhum vídeo foi encontrado
    if (videos.length === 0) {

        lista.innerHTML =
            "<li><button disabled>Nenhum vídeo encontrado.</button></li>";

        return;
    }


    // Percorre os vídeos recebidos e cria um resultado para cada um
    videos.forEach(function(video) {

        const item = document.createElement("li");

        // Monta o conteúdo que será exibido na lista
        item.innerHTML = `
            <button type="button">
                <strong>${video.titulo}</strong>
                <small>${video.duracao} · ${video.empresa}</small>
            </button>
        `;

        // Ao clicar no vídeo, exibe seus detalhes
        item.querySelector("button").onclick = function() {
            mostrarVideo(video);
        };

        lista.appendChild(item);
    });


    // Adiciona os botões de navegação entre as páginas
    adicionarPaginacao();
}


/* ---------- Paginação dos vídeos ---------- */

function adicionarPaginacao() {

    // Define a quantidade de vídeos utilizada pelo projeto
    const totalVideos = 10;
    const videosPorPagina = 5;

    // Calcula o número total de páginas
    const ultimaPagina = Math.ceil(totalVideos / videosPorPagina);

    const item = document.createElement("li");

    item.className = "paginacao";

    // Cria os botões e exibe a página atual
    item.innerHTML = `
        <button type="button" id="anterior"
            ${paginaAtual === 1 ? "disabled" : ""}>
            Anterior
        </button>

        <span>Página ${paginaAtual}</span>

        <button type="button" id="proxima"
            ${paginaAtual === ultimaPagina ? "disabled" : ""}>
            Próxima
        </button>
    `;

    lista.appendChild(item);


    // Volta uma página e realiza uma nova busca
    document.getElementById("anterior").onclick = function() {

        paginaAtual--;

        buscarVideos();
    };


    // Avança uma página e realiza uma nova busca
    document.getElementById("proxima").onclick = function() {

        paginaAtual++;

        buscarVideos();
    };
}


/* ---------- Seleção de vídeo ---------- */

async function mostrarVideo(video) {

    // Define o vídeo selecionado no player do YouTube
    document.getElementById("player-youtube").src =
        `https://www.youtube-nocookie.com/embed/${video.youtube_id}`;

    // Exibe as informações básicas do vídeo
    document.getElementById("titulo-video").textContent =
        video.titulo;

    document.getElementById("info-video").textContent =
        `Lançamento: ${video.lancamento} · Empresa: ${video.empresa}`;


    // Busca a empresa relacionada ao vídeo
    const resposta = await fetch(
        `/empresas/${video.empresa_id}`
    );

    // Converte a resposta JSON para um objeto JavaScript
    const empresa = await resposta.json();

    // Exibe os dados da empresa
    mostrarEmpresaDetalhes(empresa);


    // Procura, entre os lançamentos da empresa,
    // aquele relacionado ao vídeo selecionado
    const lancamento = empresa.lancamentos.find(function(item) {

        return item.id === video.lancamento_id;
    });

    // Exibe o lançamento encontrado
    if (lancamento) {
        mostrarLancamento(lancamento);
    }
}


/* ---------- Busca de empresas ---------- */

async function buscarEmpresas() {

    // Faz uma requisição para buscar empresas pelo nome
    const resposta = await fetch(
        `/empresas/${encodeURIComponent(termo.value)}`
    );

    // Converte a resposta JSON para um objeto JavaScript
    const empresas = await resposta.json();

    // Limpa os resultados anteriores
    lista.innerHTML = "";

    // Verifica se nenhuma empresa foi encontrada
    if (empresas.length === 0) {

        lista.innerHTML =
            "<li><button disabled>Nenhuma empresa encontrada.</button></li>";

        return;
    }


    // Percorre as empresas encontradas
    empresas.forEach(function(empresa) {

        const item = document.createElement("li");

        // Cria o resultado da empresa
        item.innerHTML = `
            <button type="button">
                <strong>${empresa.nome}</strong>
                <small>${empresa.descricao}</small>
            </button>
        `;

        // Ao clicar, busca os detalhes da empresa
        item.querySelector("button").onclick = function() {
            mostrarEmpresa(empresa.id);
        };

        lista.appendChild(item);
    });
}


/* ---------- Busca de empresa por ID ---------- */

async function mostrarEmpresa(id) {

    // Busca uma empresa diretamente pelo seu ID
    const resposta = await fetch(
        `/empresas/${encodeURIComponent(id)}`
    );

    // Verifica se a empresa não foi encontrada
    if (!resposta.ok) {

        lista.innerHTML =
            "<li><button disabled>Empresa não encontrada.</button></li>";

        return;
    }

    // Converte a resposta JSON para um objeto JavaScript
    const empresa = await resposta.json();

    // Exibe os dados da empresa
    mostrarEmpresaDetalhes(empresa);

    // Remove qualquer vídeo que esteja sendo exibido
    document.getElementById("player-youtube").src = "";

    // Exibe o nome da empresa na área do player
    document.getElementById("titulo-video").textContent =
        empresa.nome;

    // Informa a quantidade de lançamentos associados
    document.getElementById("info-video").textContent =
        `${empresa.lancamentos.length} lançamento(s)`;


    // Limpa os resultados anteriores
    lista.innerHTML = "";

    // Exibe os lançamentos relacionados à empresa
    empresa.lancamentos.forEach(function(lancamento) {

        const item = document.createElement("li");

        item.innerHTML = `
            <button type="button">
                <strong>${lancamento.nome}</strong>
                <small>${lancamento.status} · ${lancamento.foguete}</small>
            </button>
        `;

        // Ao clicar, exibe os detalhes do lançamento
        item.querySelector("button").onclick = function() {
            mostrarLancamento(lancamento);
        };

        lista.appendChild(item);
    });
}


/* ---------- Exibição dos detalhes ---------- */

function mostrarEmpresaDetalhes(empresa) {

    // Preenche os campos de informações da empresa
    document.getElementById("empresa-nome").textContent =
        empresa.nome;

    document.getElementById("empresa-descricao").textContent =
        empresa.descricao;
}


function mostrarLancamento(lancamento) {

    // Preenche os campos de informações do lançamento
    document.getElementById("lancamento-nome").textContent =
        lancamento.nome;

    document.getElementById("lancamento-data").textContent =
        lancamento.data;

    document.getElementById("lancamento-foguete").textContent =
        lancamento.foguete;

    document.getElementById("lancamento-missao").textContent =
        lancamento.missao;

    document.getElementById("lancamento-local").textContent =
        lancamento.local;

    document.getElementById("lancamento-status").textContent =
        lancamento.status;

    document.getElementById("lancamento-descricao").textContent =
        lancamento.descricao;
}