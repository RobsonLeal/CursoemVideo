# Transformar um número real em um número inteiro

from math import hypot

print('### EXERCÍCIO 17 # AULA 08 ###')
print('==============================')

oposto = float(input('Digite o cateto oposto: '))
adjacente = float(input('Digite o cateto adjacente: '))

print('A hipotenusa mede: {:.2f}'.format(hypot(oposto, adjacente)))