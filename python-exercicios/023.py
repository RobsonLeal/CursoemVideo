# Separando digitos de um número

print('### EXERCÍCIO 23 # AULA 09 ###')
print('==============================')

numero = int(input('digite um número de 1 a 9999: '))

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print('O número possui: {} unidades'.format(u))
print('O número possui: {} dezenas'.format(d))
print('O número possui: {} centenas'.format(c))
print('O número possui: {} milhar'.format(m))

print('FIM DO PROGRAMA')