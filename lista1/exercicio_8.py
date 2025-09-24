
lista = []

def inverter(texto):
    
    dividido = list(texto)
    if dividido == []:
        return lista
    texto = dividido.pop(-1)
    lista.append(texto)
    
    return inverter("".join(dividido) )


texto = "teste"
inverter(texto)
print("saida: ")
print("".join(lista))

#alocação dinamica ja esta presente na lista, ela pode crescer e variar de tamanho, diferente de um array estatico