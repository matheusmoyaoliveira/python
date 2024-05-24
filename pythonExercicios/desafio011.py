# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m²

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area= larg * alt
litros = area / 2
print('Sua parede tem dimensão de {}x{} e sua área é de {}m².'.format(larg, alt, area))
print('Para pintar essa parede, você precisará de {:.4f}l de tinta'.format(litros))