import random

def adivinha(maximo, numero_secreto):
    chute = int(input("tente adivinhar: "))
    if chute == numero_secreto:
        return print("parabens vc acertou!!!")
        
    elif chute < numero_secreto:
        nova_lista = list(range(chute+1, lista[-1]+1))
        return adivinha(nova_lista, numero_secreto)
    
    else:
        nova_lista = list(range(lista[0] ,chute))
        return adivinha(nova_lista, numero_secreto)


maximo = int(input("Para jogar selecione ate que numero, partindo do 0, vc quer tentar adivinhar: "))
lista = list(range(0, maximo+1))
numero_secreto = random.choice(lista) 
adivinha(maximo, numero_secreto)


#logica:
# 1- criar a lista no range q o usuario esolher
# 2 - um random p escolher um numero aleatorio
# 3 - usuario testa 
# 4 - verifica se é se for retorna se n perguntar se é maior ou menor 
# 5 - se for maior ajustar o intervalo do numero q o usuario deu ate o 
# range da lista e vice versa p menor tbm
#  6 - chama de novo com o valor atualizado ate acertar 

