// funcao para somar tudo até reduzir a um unico valor no final

let numeros = [1,2,3,4,5]

let somatotal = numeros. reduce(function(x,y){
    return x+y
});

console.log("Soma dos Elementos", somatotal)