num1 = int(input("digite o número inicial:"))
num2 = int(input("digite o número final: "))
div = 1
total = 0
while num1<=num2:
    while num1>div and num1!=0:
        if num1%div==0:
            total = total+div
            div += 1
        else:
            div += 1
    if total==num1 and total!=0:
        print(num1)
    num1 = num1+1
    div=1
    total =0
    
