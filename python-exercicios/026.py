# Primeira e ultima ocorrência de uma string

from unidecode import unidecode

print('### EXERCÍCIO 26 # AULA 09 ###')
print('==============================')

nome = unidecode(input('Digite uma frase: ').strip().lower())

print('A frase possui {} letras \"A\".'.format(nome.count('a')))
print('A letra "A" aparece pela primeira vez na {}ª posição.'.format(nome.find('a') + 1))
print('A letra "A" aparece pela última vez na {}ª posição.'.format(nome.rfind('a') + 1))



print('FIM DO PROGRAMA')