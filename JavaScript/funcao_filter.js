
let array1 = [10,21,32,34,53]

let pares = array1.filter(function(n){
    return n % 2 ===0;
});

console.log("Mostra numero par", pares);