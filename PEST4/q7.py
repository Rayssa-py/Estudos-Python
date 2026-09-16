soma = 0
qtd_div = 0
for num in range(2,201):
    for div in range(1,num+1):
        if num%div==0:
            qtd_div= qtd_div + 1
    if qtd_div==2:
        soma = soma+1
    qtd_div = 0
print(f"a quantidade de números de 1 a 200 que são primos é {soma}")