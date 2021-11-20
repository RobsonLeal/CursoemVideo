# Alugue de carro

print('### EXERCÍCIO 15 # AULA 07 ###')
print('==============================')

odometro = int(input('Digite a quantidade de Km rodados: '))
dias = int(input('Digite a quantidade de dia que ficou com o carro: '))

preco_km = odometro * 0.15
preco_dia = dias * 60

custo = preco_dia + preco_km

print('O valor total do veículo é de R$ {:.2f}'.format(custo))