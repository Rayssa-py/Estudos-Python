num = int(input("digite um número inteiro"))
contador = num
aux = 0
while contador != -1:
    if num>0:
        aux = contador + aux
        contador = contador-1
    elif num<0:
        aux = contador + aux
        contador = contador +1
    else:
        contador = contador -1
print(f"a soma de todos os números de {num} até -1 é:{aux}")