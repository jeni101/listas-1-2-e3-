
texto = []

undo_stack = []

def digitar(caracter):
    texto.append(caracter)
    print(f"Texto atual: {''.join(texto)}")

def desfazer():
    if texto:
        ultimo = texto.pop()          
        undo_stack.append(ultimo)    
        print(f"Undo: removeu '{ultimo}', texto agora: {''.join(texto)}")
    else:
        print("Nada para desfazer!")

def refazer():
    if undo_stack:
        refazer_caractere = undo_stack.pop()  
        texto.append(refazer_caractere)
        print(f"Redo: adicionou '{refazer_caractere}', texto agora: {''.join(texto)}")
    else:
        print("Nada para refazer!")


digitar("H")
digitar("o")
digitar("l")
digitar("a")

desfazer()
desfazer()

refazer()
digitar("!")

print(f"Texto final: {''.join(texto)}")
