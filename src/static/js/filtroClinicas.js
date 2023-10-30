const resultadoContainer = document.getElementById("resultadoContainer");
        
fetch("/static/docs/clinicas.csv")
    .then((response) => response.text())
    .then((csvData) => {
        const linhas = csvData.split("\n");
        
        document.getElementById("estadoSelect").addEventListener("change", filtrarClínicas);

        function filtrarClínicas() {
            const estadoSelecionado = document.getElementById("estadoSelect").value;
            resultadoContainer.innerHTML = "";  // Limpa o conteúdo anterior

            let estadoAtual = "";  // Para controlar o estado atual

            for (let i = 1; i < linhas.length; i++) {
                const colunas = linhas[i].split(",");
                const estado = colunas[0];
                const informacoes = colunas.slice(1);

                if (estadoSelecionado === "" || estado === estadoSelecionado) {
                    if (estado !== estadoAtual) {
                        // Adiciona o nome do estado com classe "estado" para ajustar o tamanho
                        resultadoContainer.innerHTML += `<div class="estado">${estado}</div>`;
                        estadoAtual = estado;
                    }

                    // Adiciona as informações das clínicas
                    for (let j = 0; j < informacoes.length; j++) {
                        if (j === 0) {
                            // Remove o ponto e espaço na frente do nome da clínica
                            resultadoContainer.innerHTML += `<div>${informacoes[j].replace(/^\s*\.\s*/, "")}</div>`;
                        } else {
                            // Adiciona outras informações
                            resultadoContainer.innerHTML += `<div>${informacoes[j]}</div>`;
                        }
                    }
                    
                    // Adiciona um espaço entre as clínicas
                    resultadoContainer.innerHTML += "<div>&nbsp;</div>";
                }
            }
        }
    });