

from collections import deque

fila_pedidos = deque()

def adicionar_pedido(pedido):
    fila_pedidos.append(pedido)
    print(f"Pedido '{pedido}' adicionado à fila.")

def processar_pedido():
    if fila_pedidos:
        pedido = fila_pedidos.popleft()
        print(f"Processando pedido: {pedido}")
    else:
        print("Nenhum pedido na fila.")

def listar_pedidos():
    if fila_pedidos:
        print("Pedidos na fila:")
        for i, pedido in enumerate(fila_pedidos, start=1):
            print(f"{i}. {pedido}")
    else:
        print("A fila está vazia.")


adicionar_pedido("Hambúrguer")
adicionar_pedido("Batata Frita")
adicionar_pedido("Refrigerante")

print("\n--- Situação Atual ---")
listar_pedidos()

print("\n--- Processando ---")
processar_pedido()
processar_pedido()

print("\n--- Situação Atual ---")
listar_pedidos()
