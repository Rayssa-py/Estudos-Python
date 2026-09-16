num1 = int(input("digite o primeiro número: "))
num2 = int(input("digite o segundo número: "))
num3 = int(input("digite o terceiro número: "))
if num1 == num2 == num3:
    total = (num1+num2+num3)*3
else:
    total =num1+num2+num3
print(f"o resultado é: {total}")