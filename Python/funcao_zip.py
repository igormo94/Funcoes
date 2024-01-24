##E uma função que retorna sequencia de elementos em formato de tuplas

dicverduras = {1:'Cebola',2:"Alface",3:"Repolho",4:"Beterraba"}

dicfrutas = {1:"Maçã",2:"Laranja",3:"Pera"}

print(list(zip(dicverduras.values(),dicfrutas.values())))