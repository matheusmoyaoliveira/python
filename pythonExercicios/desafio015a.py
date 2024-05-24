dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
dias = dias * 60
km = km * 0.15
total = km + dias
print('O total a pagar é de R${:.2f}'.format(total))