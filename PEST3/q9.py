num = int(input("digite um número: "))
div = 1
total = 0
while num>div:
    if num%div==0:
        total = total+div
        div += 1
    else:
        div += 1
if total==num:
    print("o número é perfeito")
else:
    print("o número não é perfeito")
