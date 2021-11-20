# Uso da função is em uma variável

print('### EXERCÍCIO 04 # AULA 06 ###')
print('==============================')

valor = input('Digite algo: ')

print('O valor é alfanumérico?', valor.isalnum())
print('O valor é composto somente por letras?', valor.isalpha())
print('O valor contém todas as letras minúsculas?', valor.islower())
print('O valor contém todas as letras maiúsculas?', valor.isupper())
