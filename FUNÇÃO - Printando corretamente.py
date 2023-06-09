"""
Nome do Programa: FUNÇÃO - Printando corretamente
Nome do Autor: Renan Lucas da Silva
Data e Hora: 24.03.23 (15h52)

    Descrição:
    Printar o valor de uma função
    Diferenciar a chamada correta da função
    
"""

def foo(a):
    return a + a + a

b = 1

foo(b)
foo(b)
foo(b)

print (b)
# aqui se printa o valor de b sozinho.

print (foo(b))
# aqui se printa o valor resultante da função.

"""
A função foo tem por objetivo retornar o triplo do valor de a.
Quando aplicamos a função foo ao valor de b
    temos como resultado o valor 3.
Porém, percebe-se que o código em nenhum momento revela na tela do usuário
    o valor da função foo sobre a variável b.
Para o valor de retorno ser 3, o código deveria ser alterado para print(foo(b)).
"""