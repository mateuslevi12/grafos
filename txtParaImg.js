const fs = require("fs");

function lerMatrizDeArquivo(caminhoArquivo) {
    const dados = fs.readFileSync(caminhoArquivo, "utf8"); // Lê o conteúdo do arquivo
    return dados.split("\n").map(linha => linha.trim().split(/\s+/).map(Number));
}

module.exports = { lerMatrizDeArquivo };
