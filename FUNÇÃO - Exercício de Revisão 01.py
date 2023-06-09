"""
Nome do Programa: FUNÇÃO - Exercício de Revisão 01
Nome do Autor: Renan Lucas da Silva
Data e Hora: 21.02.23 (06h06)

"""

def func1(x):
     x = 10
     print(x)


x = 0
print(x)
func1(x)
print(x)

# PERGUNTA: O que vai sair no console?

# 0
# 10
# 0

"""
EXPLICAÇÃO:
A variável x da linha 6 é global.
Mas, como existe outra variável com o mesmo nome dentro da função func1() – na linha 2,
apenas dentro da função func1(), x vale 10 –, chamamos essa variável de local.
Assim, o print da linha 7 recebe o valor da variável global (0).
A execução da linha 8 chama a função func1(),
que imprime o valor de x válido dentro dela (10).
Em seguida, a execução do programa sai da função func1() e
o print da linha 9 volta a enxergar a variável global x, cujo valor é 0.

"""