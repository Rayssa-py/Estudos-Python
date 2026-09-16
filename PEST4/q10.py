num = int(input("digite um número inteiro positivo: "))
soma = 0
for n in range(1,num):
		
		if n%4==0 or n%6==0:
			soma = soma + n
print(f"a soma dos divisiveis por 4 ou 6 entre 0 e {num} é {soma}")
