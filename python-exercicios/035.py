# Verifica se os valores formam um triângulo

print('### EXERCÍCIO 35 # AULA 10 ###')
print('==============================')

numeros = []

for i in range (0, 3):
    numeros.append(int(input('Digite o valor da {}ª reta do triângulo: '.format(i+1))))

numeros.sort()

if (numeros[0] + numeros[1] > numeros[2]):
    print('É possivel formar um triângulo!')
else:
    print('Não é possível formar o triângulo!')


print('FIM DO PROGRAMA!')