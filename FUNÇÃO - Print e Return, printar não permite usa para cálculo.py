"""
Nome do Programa: FUNÇÃO - Print e Return, printar não permite usa para cálculo
Nome do Autor: Renan Lucas da Silva
Data e Hora: 18.02.23 (03h23)

    Descrição:
    Retornar um valor é diferente de imprimir na tela.
    Ao utilizar a função print(), ocorre apenas a impressão de algo nela,
    o que não significa o retorno de qualquer função definida pelo usuário.
    Python não explicita diferença entre Função e Procedimento,
    permitindo que funções possam não retornar nenhum valor.
    
    PS: Função = retorna valor; Procedimento = não retorna valor;
    
"""

def func1(x):
    x = 10
    print(f'Função func1 - x = {x}')


def func2(x):
    x = 20
    print(f'Função func2 - x = {x}')
# não existe comando de RETURN aqui, portanto nenhum desses valores serão exportados para fora dao função

x = 0
func1(x)
func2(x)
print(f'Programa principal - x = {x}')

# As funções func1(x) e func2(x) não possuem qualquer retorno.
# Ou seja, elas são funções com comportamento de procedimentos.

'''
1. As linhas 1, 2 e 3 definem a função func1(x), que recebe o parâmetro x, mas tem uma variável local de nome x, cujo valor atribuído é 10;
2. Analogamente, a função func2(x) – definida nas linhas 6, 7 e 8 – recebe o parâmetro x e tem uma variável de mesmo nome, mas com valor atribuído 20;
3. O programa principal tem uma variável global de mesmo nome x, cujo valor atribuído é 0, na linha 11;
4. Veja que as chamadas às funções func1(x) e func2(x) ocorrem nas linhas 12 e 13, quando a variável x global já recebeu o valor 0. Porém, ao ser executada, cada uma dessas funções tem a própria variável local a quem todas as referências internas são feitas.
5. Mesmo com a variável global tendo valor nulo, cada variável local das funções func1(x) e func2(x) tem o próprio valor. Não há alterações na variável global mesmo com as atribuições das linhas 2 e 7.
'''