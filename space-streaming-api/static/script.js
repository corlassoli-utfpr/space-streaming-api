const form = document.getElementById("form-busca");
const tipo = document.getElementById("tipo-busca");
const termo = document.getElementById("termo");
const lista = document.getElementById("lista-resultados");

let buscaAtual = "";
let paginaAtual = 1;


/* Busca realizada pelo formulário */

form.addEventListener("submit", function(evento) {

    evento.preventDefault();

    if (tipo.value === "videos") {

        buscaAtual = termo.value;
        paginaAtual = 1;

        buscarVideos();

    } else if (tipo.value === "empresas") {

        buscarEmpresas();

    } else {

        mostrarEmpresa(termo.value);
    }
});


/* ---------- Vídeos ---------- */

async function buscarVideos() {

    const resposta = await fetch(
        `/videos/${encodeURIComponent(buscaAtual)}/${paginaAtual}`
    );

    const videos = await resposta.json();

    lista.innerHTML = "";

    if (videos.length === 0) {

        lista.innerHTML =
            "<li><button disabled>Nenhum vídeo encontrado.</button></li>";

        return;
    }


    videos.forEach(function(video) {

        const item = document.createElement("li");

        item.innerHTML = `
            <button type="button">
                <strong>${video.titulo}</strong>
                <small>${video.duracao} · ${video.empresa}</small>
            </button>
        `;

        item.querySelector("button").onclick = function() {
            mostrarVideo(video);
        };

        lista.appendChild(item);
    });


    adicionarPaginacao();
}


/* ---------- Paginação ---------- */

function adicionarPaginacao() {

    const totalVideos = 10;
    const videosPorPagina = 5;
    const ultimaPagina = Math.ceil(totalVideos / videosPorPagina);

    const item = document.createElement("li");

    item.className = "paginacao";

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


    document.getElementById("anterior").onclick = function() {

        paginaAtual--;

        buscarVideos();
    };


    document.getElementById("proxima").onclick = function() {

        paginaAtual++;

        buscarVideos();
    };
}


/* ---------- Seleção de vídeo ---------- */

async function mostrarVideo(video) {

    document.getElementById("player-youtube").src =
        `https://www.youtube-nocookie.com/embed/${video.youtube_id}`;

    document.getElementById("titulo-video").textContent =
        video.titulo;

    document.getElementById("info-video").textContent =
        `Lançamento: ${video.lancamento} · Empresa: ${video.empresa}`;


    const resposta = await fetch(
        `/empresas/${video.empresa_id}`
    );

    const empresa = await resposta.json();

    mostrarEmpresaDetalhes(empresa);


    const lancamento = empresa.lancamentos.find(function(item) {

        return item.id === video.lancamento_id;
    });

    if (lancamento) {
        mostrarLancamento(lancamento);
    }
}


/* ---------- Empresas ---------- */

async function buscarEmpresas() {

    const resposta = await fetch(
        `/empresas/${encodeURIComponent(termo.value)}`
    );

    const empresas = await resposta.json();

    lista.innerHTML = "";

    if (empresas.length === 0) {

        lista.innerHTML =
            "<li><button disabled>Nenhuma empresa encontrada.</button></li>";

        return;
    }


    empresas.forEach(function(empresa) {

        const item = document.createElement("li");

        item.innerHTML = `
            <button type="button">
                <strong>${empresa.nome}</strong>
                <small>${empresa.descricao}</small>
            </button>
        `;

        item.querySelector("button").onclick = function() {
            mostrarEmpresa(empresa.id);
        };

        lista.appendChild(item);
    });
}


/* ---------- Empresa por ID ---------- */

async function mostrarEmpresa(id) {

    const resposta = await fetch(
        `/empresas/${encodeURIComponent(id)}`
    );

    if (!resposta.ok) {

        lista.innerHTML =
            "<li><button disabled>Empresa não encontrada.</button></li>";

        return;
    }

    const empresa = await resposta.json();

    mostrarEmpresaDetalhes(empresa);

    document.getElementById("player-youtube").src = "";

    document.getElementById("titulo-video").textContent =
        empresa.nome;

    document.getElementById("info-video").textContent =
        `${empresa.lancamentos.length} lançamento(s)`;


    lista.innerHTML = "";

    empresa.lancamentos.forEach(function(lancamento) {

        const item = document.createElement("li");

        item.innerHTML = `
            <button type="button">
                <strong>${lancamento.nome}</strong>
                <small>${lancamento.status} · ${lancamento.foguete}</small>
            </button>
        `;

        item.querySelector("button").onclick = function() {
            mostrarLancamento(lancamento);
        };

        lista.appendChild(item);
    });
}


/* ---------- Exibição dos detalhes ---------- */

function mostrarEmpresaDetalhes(empresa) {

    document.getElementById("empresa-nome").textContent =
        empresa.nome;

    document.getElementById("empresa-descricao").textContent =
        empresa.descricao;
}


function mostrarLancamento(lancamento) {

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