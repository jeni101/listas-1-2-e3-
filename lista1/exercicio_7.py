
LINHAS = 5
COLUNAS = 10

teatro = [[0 for _ in range(COLUNAS)] for _ in range(LINHAS)]

def mostrar_teatro():
    print("\nMapa de assentos (0 = livre, 1 = reservado):")
    for i in range(LINHAS):
        print(f"Fileira {i+1}: {teatro[i]}")
    print()

def reservar_assento(linha, coluna):
    if teatro[linha][coluna] == 0:
        teatro[linha][coluna] = 1
        print(f"Assento {coluna+1} da fileira {linha+1} foi reservado com sucesso.")
    else:
        print(f"O assento {coluna+1} da fileira {linha+1} já está reservado.")

def cancelar_reserva(linha, coluna):
    if teatro[linha][coluna] == 1:
        teatro[linha][coluna] = 0
        print(f"Reserva do assento {coluna+1} da fileira {linha+1} foi cancelada.")
    else:
        print(f"O assento {coluna+1} da fileira {linha+1} já está livre.")


mostrar_teatro()
reservar_assento(0, 3)  
reservar_assento(2, 5)  
mostrar_teatro()
cancelar_reserva(0, 3)  
mostrar_teatro()

#logica: 
# criar a matriz (todos assentos livres = 0)
# mostrar todos os assentos 
# reservar o assento e atualizar o valor (reservado = 1)
# cancelar reserva volta o valor original 