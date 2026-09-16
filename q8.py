#Questão 08
medida = input("Qual a unidade de medidas que quer converter?(metros,centimetros,milhas) ")
valor = float(input("Digite o valor: "))
convert = input("Para o qual quer converter? (metros,centimetros ou milhas)")
if medida == "milhas" and convert == "metros":
 	result = valor*1609.344
elif medida == "metros" and convert == "milhas":
 	result = valor/1609.344
elif medida == "milhas" and convert == "centimetros":
 	result = valor*160934.4
elif medida == "centimetros" and convert == "milhas":
 	result = valor/160934.4
elif medida == "metros" and convert == "centimetros":
 	result = valor*100
elif medida == "centimetros" and convert == "metros":
 	result = valor/100
elif medida == convert:
	result = valor
else:
 	result = "não foi possivel fazer a conversão, unidade de medida incorreta."
print(f"Conversão: {result}")
