from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
sexo = str(input('Qual o seu genero? '))
idade = atual - nasc
if sexo in 'Mulher mulher Feminino feminino':
    print('Você não precisa fazer o alistamento militar obrigatório')
else:
    print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        print('Ainda faltam {} anos para o alistamento'.format(saldo))
        ano = atual + saldo
        print('Seu alistamento será em {}'.format(ano))
    elif idade > 18:
        saldo = idade - 18
        print('Você já deveria ter se alistado há {} anos.'.format(saldo))
        ano = atual - saldo
        print('Seu alistamento foi em {}'.format(ano))

