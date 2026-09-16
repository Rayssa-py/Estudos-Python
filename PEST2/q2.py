#questão 2
idade = int(input("digite sua idade: "))
if idade >= 60:
    idade = "idoso"
elif idade >= 18 and idade < 60 :
    idade = "adulto"
elif idade >=12 and idade<18:
    idade = "adolescente"
else:
    idade = "criança"
print(f"de acordo com sua idade você é um(a) {idade}")