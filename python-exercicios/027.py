# Separando o último e o primeiro nome

print('### EXERCÍCIO 27 # AULA 09 ###')
print('==============================')

nome_completo = input('Digite seu nome completo: ')

nome_separado = nome_completo.split()

nome_formatado = "{} {}".format(nome_separado[0], nome_separado[len(nome_separado) - 1])

print('Bem vindo!', nome_formatado)

print('FIM DO PROGRAMA')