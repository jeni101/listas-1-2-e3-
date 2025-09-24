
lista = []

def inverter(texto):
    
    dividido = list(texto)
    if dividido == []:
        return lista
    texto = dividido.pop(-1)
    lista.append(texto)
    
    return inverter("".join(dividido) )


texto = "teste"
inverter(texto)
print("saida: ")
print("".join(lista))

# logica: 
# 1- passa o texto escolhido
# 2- separa as letras
# 3- verifica se essa lista esta vazia
# 4 - se n estiver tira a ultima atualiza o texto letra a adiciona a letra em uma lista 
# 5- retorna a funcao com o texto atualizado
# 6- .join p juntar tudo quando acabar 