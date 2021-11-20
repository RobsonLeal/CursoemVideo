# Conversor de temperatura

print('### EXERCÍCIO 14 # AULA 07 ###')
print('==============================')

celsius = int(input('Digite a temperatura(ºC): '))

fahrenheit = 32 + (celsius * (9/5))

print('{}ºC é equivalente a {:.2f}ºF'.format(celsius, fahrenheit))
