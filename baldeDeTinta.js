const fs = require("fs");
const { lerMatrizDeArquivo } = require("./txtParaImg");

function baldeDeTintaBFS(imagem, linhaInicial, colunaInicial, novaCor) {
    const totalLinhas = imagem.length;
    const totalColunas = imagem[0].length;
    const corOriginal = imagem[linhaInicial][colunaInicial];

    if (corOriginal === novaCor) return imagem; // Se a cor for a mesma, não há o que modificar.

    // Fila para BFS
    let fila = [[linhaInicial, colunaInicial]];
    imagem[linhaInicial][colunaInicial] = novaCor;

    // Direções para os 8 vizinhos (Chebyshev)
    const direcoes = [
        [-1, 0], [1, 0], [0, -1], [0, 1],  // Cima, Baixo, Esquerda, Direita
        [-1, -1], [-1, 1], [1, -1], [1, 1] // Diagonais
    ];

    while (fila.length > 0) {
        let [linha, coluna] = fila.shift(); // Remove o primeiro da fila

        for (let [deslocLinha, deslocColuna] of direcoes) {
            let novaLinha = linha + deslocLinha;
            let novaColuna = coluna + deslocColuna;

            // Verifica se está dentro dos limites da matriz e se a cor é igual à original
            if (
                novaLinha >= 0 && novaLinha < totalLinhas &&
                novaColuna >= 0 && novaColuna < totalColunas &&
                imagem[novaLinha][novaColuna] === corOriginal
            ) {
                imagem[novaLinha][novaColuna] = novaCor; // Pinta o pixel
                fila.push([novaLinha, novaColuna]); // Adiciona à fila
            }
        }
    }

    return imagem;
}

const imagem = lerMatrizDeArquivo("data/UNIFOR_grayscale.txt");

// Parâmetros de entrada
let linhaInicial = 5, colunaInicial = 7, novaCor = 2;

console.log("Matriz original:");
console.log(imagem.map(linha => linha.join(" ")).join("\n"));

// Aplicar o Balde de Tinta
let resultado = baldeDeTintaBFS(imagem, linhaInicial, colunaInicial, novaCor);

console.log("\nMatriz após preenchimento:");
console.log(resultado.map(linha => linha.join(" ")).join("\n"));

// **Salvar o resultado em um arquivo TXT**
const caminhoSaida = "data/matriz_preenchida.txt";

fs.writeFileSync(caminhoSaida, resultado.map(linha => linha.join(" ")).join("\n"), "utf8");

console.log(`\nMatriz preenchida salva em: ${caminhoSaida}`);
