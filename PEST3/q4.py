num = float(input("digite um número: ")) 
contador = 0
result = 0
while num!=0:
    if result <100:
        result = contador*num
        print(result)
    else:
        num = float(input("digite um número: "))
