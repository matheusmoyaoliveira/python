times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Bahia',
         'Cruzeiro', 'São Paulo', 'Fortaleza', 'Athletico-PR',
         'Bragantino', 'Atlético-MG', 'Vasco da Gama', 'Juventude',
         'Internacional', 'Criciúma', 'Cuiabá', 'EC Vitória',
         'Corinthians', 'Grêmio', 'Atlético-GO', 'Fluminense')
# for t in times:
#   print(t)
print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabéticas: {sorted(times)}')
print('-=' * 15)
print(f'O Corinthians está na {times.index("Corinthians")+1}ª posição')
