# Analisador de nome

print('### EXERCÍCIO 22 # AULA 09 ###')
print('==============================')

nome = input('Digite o seu nome completo: ').strip()


print('Todas as letras do nome maiúsculas: ', nome.upper())
print('Todas as letras do nome minúsculas: ', nome.lower())
print('Tamanho do nome sem espaços: ', len(nome) - nome.count(' '))
print('Tamanho do primeiro nome: ', nome.find(' '))
#print('Tamanho do primeiro nome: ', len(nome.split()[0]))

print('FIM DO PROGRAMA')
