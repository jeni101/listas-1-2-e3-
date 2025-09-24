def caminho_minimo(matriz, origem, destino, visitado=None):
    if visitado is None:
        visitado = set()
    
    x, y = origem
    dx, dy = destino

    
    if (x < 0 or y < 0 or x >= len(matriz) or y >= len(matriz[0]) or matriz[x][y] == 1):
        return float('inf')
    
    
    if (x, y) in visitado:
        return float('inf')
    
  
    if (x, y) == destino:
        return 0
    
    visitado.add((x, y))

    movimentos = [(-1,0), (1,0), (0,-1), (0,1)]
    
    distancias = []
    for dx_move, dy_move in movimentos:
        proximo = (x + dx_move, y + dy_move)
        distancia = 1 + caminho_minimo(matriz, proximo, destino, visitado.copy())
        distancias.append(distancia)
    
    return min(distancias)
