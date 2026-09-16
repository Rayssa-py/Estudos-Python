import random 
num = random.randint(10,50)
num1 = int(input("digite um número entre 10 e 50: "))
while num1 != num:
    if num1 > num:
        print("o número digitado é maior que o número secreto")
    else:
        print("o número digitado é menor que o número secreto")
    num1 = int(input("digite um número entre 10 e 50: "))
print("parabéns você achou o número secreto!")