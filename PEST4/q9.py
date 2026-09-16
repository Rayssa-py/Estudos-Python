num1 = int(input("Digite o número inicial: "))
num2 = int(input("Digite o número final: "))

div = 1
dig = 0
dig_aux = 0
qtd_dig = 0
soma =0
qtd_narc = 0

for n in range(num1,num2+1):
	num = n
	while num>0:
		dig_aux = ((num//div)%10)
		num = num - (dig_aux*div)
		div = div*10
		qtd_dig = qtd_dig + 1
		
	num = n
	div = 1
	dig_aux = 0
	
	while num>0:
		dig_aux = ((num//div)%10)
		soma =(dig_aux**qtd_dig)+soma
		num = num - (dig_aux*div)
		div = div*10
	if n == soma:
		qtd_narc = qtd_narc + 1
		print(f"{n} é um número narcisista")
		
	div = 1
	dig = 0
	dig_aux = 0
	qtd_dig = 0
	soma =0
	
print(f"existe {qtd_narc} nesse intervalo")
