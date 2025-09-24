from collections import deque
import random
import time

fila = deque()

clientes = ["Alice", "Bob", "Carol", "David", "Eva"]
for cliente in clientes:
    fila.append(cliente)
    print(f"{cliente} entrou na fila.")


while fila:
    cliente_atendido = fila.popleft()  
    tempo_atendimento = random.randint(2, 5)  
    print(f"\nAtendendo {cliente_atendido} (tempo estimado: {tempo_atendimento}s)...")
    time.sleep(tempo_atendimento) 
