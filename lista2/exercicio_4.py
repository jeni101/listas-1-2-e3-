def carregar_dados():
    print("Carregando dados na memória...")
    dados = [
        {"nome": "Alice", "idade": 25},
        {"nome": "Bob", "idade": 30},
        {"nome": "Carol", "idade": 22}
    ]
    return dados

dados_em_memoria = None

def obter_dados():
    global dados_em_memoria
    if dados_em_memoria is None:
        dados_em_memoria = carregar_dados()
    return dados_em_memoria

# ---------- Uso ----------
print("Programa iniciado")


print("\nSolicitando dados pela primeira vez:")
dados = obter_dados()  
print(dados)

print("\nSolicitando dados novamente:")
dados = obter_dados() 
