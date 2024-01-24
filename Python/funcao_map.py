## A funcao Map tem como objetivo aplicar função ou uma ação em todos os elementos 
#em uma estrutura de dados, retornando uma nova sequencia ou resultados

import math

lista = [1,5,3,15,78]

def soma(x):
    return x+2

print(tuple(map(soma,lista)))

print(list(map(soma,lista)))

print(list(map(math.sqrt,lista)))