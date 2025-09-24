def calcular_rpn(expressao):
    pilha = []
    operadores = "+-*/"
    
    for token in expressao.split():  
            
            pilha.append(float(token))
    else:
        
            b = pilha.pop()
            a = pilha.pop()
            
            if token == '+':
                resultado = a + b
            elif token == '-':
                resultado = a - b
            elif token == '*':
                resultado = a * b
            elif token == '/':
                resultado = a / b
            
            pilha.append(resultado)
    
    return pilha[0] 


expressao = "3 4 + 2 * 7 /"  # equivalente a ((3 + 4) * 2) / 7
print(f"Expressão: {expressao}")
print(f"Resultado: {calcular_rpn(expressao)}")
