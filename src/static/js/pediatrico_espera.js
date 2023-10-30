const tabelaEstado = document.getElementById("tabelaEstado");
const filtroEstado = document.getElementById("filtroEstado");
const estadoHeader = document.getElementById("estadoHeader");
const pacientesHeader = document.getElementById("pacientesHeader");

// Carrega o arquivo CSV
fetch("/static/docs/pediatrico_espera.csv")
    .then((response) => response.text())
    .then((csvData) => {
        // Converte o CSV em um array de objetos
        const linhas = csvData.split("\n");
        const data = [];
        for (let i = 1; i < linhas.length - 1; i++) {
            const colunas = linhas[i].split(",");
            data.push({ estado: colunas[0], pacientes: colunas[1] });
        }

        // Preenche a tabela com os dados
        data.forEach((item) => {
            const linha = document.createElement("tr");
            linha.setAttribute("data-estado", item.estado);
            linha.innerHTML = `
                <td>${item.estado}</td>
                <td>${item.pacientes}</td>
            `;
            tabelaEstado.appendChild(linha);
        });

        // Oculta todas as linhas da tabela
        const linhasTabela = tabelaEstado.querySelectorAll("tr");
        linhasTabela.forEach((linha) => {
            linha.style.display = "none";
        });

        // Evento de alteração do select
        filtroEstado.style.display = "block"; // Mostra o seletor
        filtroEstado.addEventListener("change", () => {
            const estadoSelecionado = filtroEstado.value;

            // Oculta todas as linhas
            linhasTabela.forEach((linha) => {
                linha.style.display = "none";
            });

            if (estadoSelecionado === "MostrarTodos") {
                // Mostra todas as linhas
                linhasTabela.forEach((linha) => {
                    linha.style.display = "table-row";
                });
            } else if (estadoSelecionado) {
                // Exibe a linha correspondente ao estado selecionado
                const linhaSelecionada = tabelaEstado.querySelector(`[data-estado="${estadoSelecionado}"]`);
                linhaSelecionada.style.display = "table-row";
            }

            // Exibe as colunas de "Estado" e "Pacientes" quando uma opção é selecionada
            estadoHeader.style.display = "table-cell";
            pacientesHeader.style.display = "table-cell";
        });
    });
