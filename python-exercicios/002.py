#Programa que exibe uma mensagem na tela, concatenendo com uma variável

print('### EXERCÍCIO 02 # AULA 05 ###')
print('==========++==================')

nome = input('Digite o seu nome: ')

print('Seja bem vindo!', nome)

#String interpolation
print('Seja bem vindo! {:=^20}'.format(nome))
