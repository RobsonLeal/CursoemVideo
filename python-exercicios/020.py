# Soteando alunos para apresentar trabalho

from random import shuffle

print('### EXERCÍCIO 20 # AULA 08 ###')
print('==============================')

alunos = []

for i in range (0, 4):
    alunos.append(input('Digite o nome do aluno: '))
    
shuffle(alunos)

print('A ordem da aprensentação é: ')

for i in range (0, 4):
    print(alunos[i])
