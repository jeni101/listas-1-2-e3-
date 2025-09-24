#logica:
# percorrer a lista e direcionar os parenteses em 2 listas separadas:
# abertura (,{,[,   e  )}] fechamento
# um dicionario com os pares correspondentes para auxiliar melhor 

# fazer condicionais para verificar se o primeiro parenteses de fechamento combina com o ultimo de abertura
# se n tiver abertura retorna false ou um print de erro pois falta parentesses 
# pegar o ultimo item da lista abertura e verifica a o par dele no dicionario é correspondente com o de fechamento
# verificar se resta algo na abertura dps das verificacoes
# a ver:
# mudar a saida se true para algum print ou n?  

abertura = []
fechamento = []
pares = {"(": ")", "{": "}", "[": "]"}

def verificacao(expressao):
    for i in expressao:
        if i == "(" or i == "{" or i == "[":
            abertura.append(i)
        
        if i == ")" or i == "}" or i == "]":
            fechamento.append(i)
            if not abertura:
                return False  
            
            if i == pares[abertura[-1]]: 
                abertura.pop() 
            else:
                return False 
   
    return len(abertura) == 0


expressao = "({[]})"
print(verificacao(expressao))  
