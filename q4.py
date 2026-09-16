relogio = int(input("digite o horário atual (número inteiro): "))
tocar = int(input("digite em quantas horas o alarme irá tocar: "))
alarme = 0

while alarme<tocar:
    relogio = relogio + 1
    alarme = alarme + 1
    if relogio == 24:
        relogio =0
    else:
        relogio = relogio
print(f"alarme... já são {relogio} horas!")