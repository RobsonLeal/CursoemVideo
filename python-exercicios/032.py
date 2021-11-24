# Verificar se um ano é bisexto

from datetime import date

print('### EXERCÍCIO 32 # AULA 10 ###')
print('==============================')

ano = int(input('Digite um ano para analisar: (Digite 0 para o ano atual) '))

if ano == 0:
    ano = date.today().year

if (ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0):
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))

print('FIM DO PROGRAMA')