num = int(input("digite um número: "))
if num > 0:
    num = "positivo"
elif num < 0:
    num = "negativo"
else:
    num = "neutro"
print(f"o número digitado é {num}")