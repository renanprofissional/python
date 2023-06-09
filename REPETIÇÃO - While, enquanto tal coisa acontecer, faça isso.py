# REPETIÇÃO - While, enquanto tal coisa acontecer, faça isso


palavra = input('Entre com uma palavra: \n ')
while palavra != 'sair':
    palavra = input('Digite mais uma palavra ou digite "sair" para encerrar o laço: \n')
print('Você digitou sair e agora está fora do laço')