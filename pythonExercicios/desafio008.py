# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

v = float(input('Uma distância em metro: '))
km = v * 0.001
hm = v * 0.01
am = v * 0.1
dm = v * 10
cm = v * 100
mm = v * 1000
print('A medida de {:.1f}m corresponde a '
      '\n{:.3f}km '
      '\n{:.2f}hm '
      '\n{:.1f}am '
      '\n{:.0f}dm '
      '\n{:.0f}cm '
      '\n{:.0f}mm'.format(v, km, hm, am, dm, cm, mm))