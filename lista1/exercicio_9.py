#logica:
# dicionario com o nome e numero de telefone (é dinamico e ja tem os dois valores q preciso)
# buscar pela chave nome e retornar o nome e telefone 
# colocar uma condicional so p verificar o tamanho do numero de telefone e se é int 
# inserir = nome: telefone 
# retirar dps atualiza o dicionario 

lista_telefonica = {}

def incerir(nome, telefone):
    lista_telefonica[nome] = telefone
    print("contato adicionado com sucesso!")
    
def deletar(nome):
    if nome in lista_telefonica:
        del lista_telefonica[nome]
        print(f"{nome} foi deletado com sucesso!")
    else:
        print("usuario não encontrado")

def buscar(nome):
    if nome in lista_telefonica:
        print("pessoa encontrada: \n")
        print(f"{nome}: {lista_telefonica[nome]}")
    
    else:
        print("pessoa nao encontrada")


        

        

incerir("cleiton", 242424242)
incerir("cleitin", 7878787878)
buscar("cleiton")

deletar("cleiton")
buscar("cleiton")
