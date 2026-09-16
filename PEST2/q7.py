num = int(input("digite um número de quatro digitos: "))
dig1 = num%10
dig2= (num//10)%10
dig3 = (num//100)%10
dig4 = (num//1000)%10
print(f"{dig1}{dig2}{dig3}{dig4}")

if dig1 == dig4 and dig2 == dig3:
    print("este é um número espelho")
else:
    print("este não é um número espelho")