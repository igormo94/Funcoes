#Retorna indice de uma colecao de dados

animais = ["Cachorro","Gato","Elefante","Papagaio"]

print(list(enumerate(animais)))

# Iterar uma lista com enumerate

for i, valor in enumerate(animais):
    print(i,valor)

#Iterador com condicionais
    
for i, valor in enumerate (animais):
    if i>2:
        break
    else:
        print(valor)