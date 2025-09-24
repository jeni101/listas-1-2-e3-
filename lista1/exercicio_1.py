import os  # já vem no Python, não é externo

def listar_diretorio(dataway, nivel=0):
    """Lista recursivamente os arquivos e pastas a partir do caminho dado"""
    try:
        for item in os.listdir(dataway):             
            caminho_item = os.path.join(dataway, item)  
            print("   " * nivel + "- " + item)       
            if os.path.isdir(caminho_item):          
                listar_diretorio(caminho_item, nivel + 1)
    except PermissionError:
        print("   " * nivel + "[Acesso negado]")

dataway = "colocar o caminho"
listar_diretorio(dataway)
