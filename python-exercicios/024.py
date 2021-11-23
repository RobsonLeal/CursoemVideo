# Verificando as primeiras letras de um texto

print('### EXERCÍCIO 24 # AULA 09 ###')
print('==============================')

cidade = input('Digite o nome de sua cidade: ').title().strip()
eHsanto = cidade.find('Santo')

print('Nome da cidade começa com Santo?', eHsanto == 0 and 'Sim' or 'Não')

print('FIM DO PROGRAMA')