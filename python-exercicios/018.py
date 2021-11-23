# Calcula a hipotenusa de um triângulo

import math

print('### EXERCÍCIO 18 # AULA 08 ###')
print('==============================')

angulo = math.radians(float(input('Digite o valor de um ângulo: ')))

sen = math.sin(angulo)
cos = math.cos(angulo)
tan = math.tan(angulo)

print('O valor do seu seno é: {:.2f}'.format(sen))
print('O valor do seu coseno é: {:.2f}'.format(cos))
print('O valor da sua tangente é: {:.2f}'.format(tan))