#função filter filtra elementos de uma estrutura de dados
# E filtra o valor que queremos encontrar

listamista = [1,"João","Pedro",53]

def busca(x):
    return x == "João"

#Não otimizada
print(list(filter(busca,listamista)))

#Forma Otimizada
print(list(filter(lambda x: x == "João",listamista)))