# Programa da adivinhação

from random import randrange
from time import sleep

print('### EXERCÍCIO 28 # AULA 10 ###')

print('-=-' * 18)
print('Vou pensar em um número entre 0 e 5, tente adivinhar!')
print('-=-' * 18)

numero_secreto = randrange(0, 6)

chute = int(input('Digite um número: '))

print('PROCESSANDO ...')
sleep(2)

valido = chute <= 5 and chute >= 0

if valido:
    if chute == numero_secreto and valido:
        print('Parabêns! Você acertou!')
    else:
        print('Você errou! O número secreto era: ', numero_secreto)

else:
    print('Número inválido!')

print('FIM DO PROGRAMA')