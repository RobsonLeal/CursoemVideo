# Exibe tabuada

print('### EXERCÍCIO 09 # AULA 07 ###')
print('==============================')

numero = int(input('Digite um número inteiro: '))

for i in range (0, 11):
    print('{:>2} x {:>2} = {:>2}'.format(numero, i, numero * i))
    