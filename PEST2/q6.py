num = int(input("digite um número de quatro digitos: "))
dig1 = num%10
dig2 = ((num//10)%10)
dig3 = ((num//100)%10)
dig4 = ((num//1000)%10)
if dig1 != dig2 and dig2 !=dig3 and dig3!=dig4 and dig1!=dig4 and dig1 != dig4:
    print("todos os números são diferentes")
else:
    print("existe algum número igual")
