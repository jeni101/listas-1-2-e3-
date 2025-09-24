def multiplicar(a,b):
    if b == 0:
        return 0 
    return a + multiplicar(a, b-1)

resultado = multiplicar(2,4)
print(resultado)
# logica:
# 1- pedir a entrada 
# 2- somar o primeiro numero e subtrair 1 do numero q esta multiplicando 
# 3- chame de novo 