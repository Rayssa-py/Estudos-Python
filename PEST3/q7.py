num = 1
while num <=50:
    if num%4==0 and num%6==0:
        print("quad")
    elif num%6==0:
        print('hex')
    elif num%4==0:
        print("quadhex")
    else:
        print(num)
    num += 1
