num = int(input("digite um numero de 5 digitos: "))
result = ((num%10)+((num//10)%10)+((num//100)%10)+((num//1000)%10)+((num//10000)%10))
print(f"A soma de todos os digitos é: {result}")
