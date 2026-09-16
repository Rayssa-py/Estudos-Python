num = int(input("digite um número: "))
if 50 < num < 100:
    num = "é entre 50 e 100"
elif num < 0 or num > 200:
    num = "é menor que 0 ou maior que 200"
else:
    num = "está fora das condições anteriores"
print(f" o número {num}")