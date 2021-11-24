# Radar de velocidade

print('### EXERCÍCIO 29 # AULA 10 ###')
print('==============================')

velocidade = int(input('Digite a velocidade do carro: '))

limite_velocidade = 80

if velocidade <= limite_velocidade:
    print('\033[1;30;42mVocê está dentro do limite!\033[m')
else:
    multa = (velocidade - limite_velocidade) * 7
    print('\033[1;30;41mVocê foi multado! Valor da multa R$ {:.2f}\033[m'.format(multa))

print('FIM DO PROGRAMA')