num = int(input("digite um número: "))
total=0
for n in range(1,num):
    if num%n==0:
        total=total+n
if total==num:
    print(f"{num} é perfeito")
else:
    print(f"{num} não é perfeito")
    