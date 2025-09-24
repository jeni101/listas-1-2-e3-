
inventario = {}

def mostrar_inventario(inv):
    if not inv:
        print("\nInventário vazio.\n")
        return
    print("\n--- Inventário Atual ---")
    for item, info in inv.items():
        print(f"{item}: quantidade = {info['quantidade']}, preço = R${info['preco']:.2f}")
    print("-----------------------\n")


def atualizar_item(item):
    print(f"\nAtualizando item: {item}")
    quantidade = int(input("Nova quantidade: "))
    preco = float(input("Novo preço: "))
    item["quantidade"] = quantidade
    item["preco"] = preco
    print("Item atualizado com sucesso!")


def adicionar_item(inv, nome):
    if nome in inv:
        print("Item já existe!")
        return
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: "))
    inv[nome] = {"quantidade": quantidade, "preco": preco}
    print(f"Item '{nome}' adicionado!")

while True:
    print("\n1 - Mostrar inventário")
    print("2 - Adicionar item")
    print("3 - Atualizar item")
    print("4 - Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        mostrar_inventario(inventario)
    
    elif escolha == "2":
        nome_item = input("Nome do item a adicionar: ")
        adicionar_item(inventario, nome_item)
    
    elif escolha == "3":
        nome_item = input("Nome do item a atualizar: ")
        if nome_item in inventario:
            atualizar_item(inventario[nome_item])
        else:
            print("Item não encontrado!")
    
    elif escolha == "4":
        print("Saindo...")
        break
    
    else:
        print("Opção inválida!")
