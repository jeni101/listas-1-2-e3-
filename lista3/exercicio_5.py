historico = []


MAX_HISTORICO = 5


def jogar(jogada):
    if len(historico) == MAX_HISTORICO:
        historico.pop(0)  # remove a jogada mais antiga
    historico.append(jogada)
    print(f"Jogada realizada: {jogada}")


def voltar():
    if historico:
        ultima = historico.pop()
        print(f"Voltando à jogada anterior: {ultima}")
    else:
        print("Nenhuma jogada para voltar!")

# ---------- Simulação ----------
jogar("andar para frente")
jogar("pular")
jogar("virar à esquerda")
jogar("coletar item")
jogar("atacar inimigo")
jogar("andar para trás")  

print("\nHistórico atual:", historico)

voltar()  
print("Histórico após voltar:", historico)
