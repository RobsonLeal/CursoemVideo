# Calcula valor da passagem

print('### EXERCÍCIO 31 # AULA 10 ###')
print('==============================')

distancia = int(input('Digite a distância a ser percorrida na sua viagem: '))

preco = distancia * 0.5 if distancia <= 200 else distancia * 0.45 

print('Sua viagem vai custar R$ {:.2f}'.format(preco))

print('FIM DO PROGRAMA')