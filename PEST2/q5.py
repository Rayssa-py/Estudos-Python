num = int(input("digite um número: "))
if num%4==0 and num%5==0:
    print("o número digitado é divisível por 4 e 5.")
elif num%5==0:
    print("número divisível por 5.")
elif num%4==0:
    print("o número digitado é divisível por 4.")
else:
    print("o número digitado não divisível nem por 4 e nem por 5.")