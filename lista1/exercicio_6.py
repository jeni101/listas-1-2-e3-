#logica:
# terá 3 torres
# 5 discos = 5 numeros de 1-5 sendo o 1 o ultimo 
# verificar se o ultimo disco e o primeito estao na torre final e as outras torres estao vazias
# verificacao se as torres de intermediario e final estao vazias,se estiverem o 1 sai 
# depois vai para o proximo e verifica se ele é menor q oq esta la se for coloca se n procura outra torre 
# chama a funcao toda de novo p organizar oq tem nela 
# proximo item (esses dois passos ficarao em loop)

def torre_de_hanoi(numero_de_discos, torre_inicial, torre_intermediaria, torre_final):
    if numero_de_discos ==1:
        print(f"Mover disco 1 da torre {torre_inicial} para a torre {torre_final}")
        return
    torre_de_hanoi(numero_de_discos -1, torre_inicial, torre_final, torre_intermediaria)
    print(f"Mover disco {numero_de_discos} da torre {torre_inicial} para a torre {torre_final}")
    torre_de_hanoi(numero_de_discos-1, torre_intermediaria, torre_inicial, torre_final)
 
n_discos = 5
torre_de_hanoi(n_discos, "A", "B", "C")
 
 