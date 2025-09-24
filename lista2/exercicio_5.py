def trocar(valores):
    valores[0], valores[1] = valores[1], valores[0]

nums = [10, 20]
trocar(nums)
print("nums:", nums)  
