# Exibe um número, seu antecessor e seu sucessor

print('### EXERCÍCIO 05 # AULA 07 ###')
print('==============================')

numero = int(input('Digite um número: '))

print('O número digitado foi: {:>02}. Seu antecessor é {:>02} e seu sucessor é {:>02}'.format(numero, numero-1, numero+1))
