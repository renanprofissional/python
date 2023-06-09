"""
Nome do Programa: FUNÇÃO - Global, forçando as funções a alterarem variáveis globais
Nome do Autor: Renan Lucas da Silva
Data e Hora: 20.02.23 (02h21)

    Descrição:
    Existem dois escopos: global e local.
    Variáveis globais e parâmetros locais podem acontecer de terem os mesmos nomes.
    Quando uma função se utiliza de um parâmetro de nome 'x' e globalmente também existe uma variável de nome 'x', a função não altera a variável global.
    A função está referenciando um parâmetro próprio, não a variável global.
    Para referenciar e alterar a variável global, é necessário um comando próprio, uma função chamada "global".
    
"""

'''
***EXEMPLO ONDE AS FUNÇÕES NÃO MEXEM NA VARIÁVEL GLOBAL***
def func1(x):
    x = 10
    print(f'Função func1 - x = {x}')


def func2(x):
    x = 20
    print(f'Função func2 - x = {x}')


x = 0
func1(x)
func2(x)
print(f'Programa principal - x = {x}')
'''

# nesse caso abaixo as funções alteram diretamente o valor da variável global
# X começa com valor 0, depois da função1 é 10, depois da func2 é 20.
def func1():
    global x
    x = 10
    print(f'Função func1 - x = {x}')


def func2():
    global x
    x = 20
    print(f'Função func2 - x = {x}')


x = 0
func1()
func2()
print(f'Programa principal - x = {x}')