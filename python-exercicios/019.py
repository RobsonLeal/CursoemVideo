# Soteando alunos para apagar o quadro

from random import randrange

print('### EXERCÍCIO 19 # AULA 08 ###')
print('==============================')

alunos = []

for i in range (0, 4):
    alunos.append(input('Digite o nome do aluno: '))
    
print('O sorteado para apagar o quadro foi: ', alunos[randrange(0, 4)])
