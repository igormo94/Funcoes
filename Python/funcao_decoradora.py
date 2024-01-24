# funcoes decoradoras potencializam ou modificam a logica de 
# outra funcao ou metodo.

# uma funcao decoradora e quando utilizamos o @ em cima de uma funcao

#exemplo

# @ decoradora
# def oi():
# print('oi')

## Criar uma funcao decoradora

def master(msg):
    def imprime():
        print("esse e a funcao decoradora")
    msg()
    return imprime

#criar uma funcao que vai receber a decoradora
@master
def chama_funcao():
    print("esta está chamando a funcao real")

## chamando a funcao
    
chama_funcao()