# Verifica o qual o maio e o menor valor

print('### EXERCÍCIO 33 # AULA 10 ###')
print('=='*15)

numeros = []

for i in range (1, 4):
    numeros.append(int(input('Digite o {}º número: '.format(i))))

numeros.sort()

print('O menor número é:', numeros[0])
print('O maior número é:', numeros[2])

print('FIM DO PROGRAMA!')