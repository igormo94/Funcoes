## Ela reduz um iteravel a um unico valor final

from functools import reduce

lista = [2,7,10,3,78]

def mult(x,y):
    return x*y

print(reduce(mult,lista))

#testa maior valor com reduce

lista2 = [2,68,42,89,600,12]

testemaior = lambda x,y : x if (x>y) else y

print(reduce(testemaior,lista2))

