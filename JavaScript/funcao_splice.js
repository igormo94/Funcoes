// A funcao splice altera o array. Remove e substitui elementos.

// remover 1 elemento a partir da posição  2 do indice de memoria

let numeros = [1,2,3,4,5]

numeros.splice(2,1)

console.log("Resultado Remoção", numeros);

let numeros2 = [1,2,3,4,5]

numeros2.splice(2,2,500,100)

console.log("resultados Substituição ARray", numeros2)