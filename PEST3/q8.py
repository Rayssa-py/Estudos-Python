num = int(input("digite o número que deseja converter: "))
total = 0
posicao = 1
while num>0:
    result = (num%2)*posicao
    total = total + result
    num = num // 2
    posicao = posicao*10
print(f"o número binário é: {total}")
    