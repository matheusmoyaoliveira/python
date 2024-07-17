lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

for cont in range(0, len(lanche)): # Usado para mostrar a posição
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for ps, comida in enumerate(lanche): # Usado para mostrar a posição #2
    print(f'Eu vou comer {comida} na posição {cont}')

for comida in lanche: # Não da para mostrar a posição
   print(f'Eu vou comer {comida}')

print(sorted(lanche)) # De forma ordenada alfabéticamente
print(lanche)

print('Comi pra caramba!')
