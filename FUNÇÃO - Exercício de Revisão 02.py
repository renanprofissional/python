"""
Nome do Programa: FUNÇÃO - Exercício de Revisão 02
Nome do Autor: Renan Lucas da Silva
Data e Hora: 21.02.23 (06h12)

"""

def rec(n):
     if n < 2:
          return rec(n - 1)


print(rec(1))

#PERGUNTA: Quando o usuário tentou executar esse programa, houve um erro. Qual é a causa?

#execução infinita à números negativos = recursos/memória excedida

'''
A função é recursiva, mas não apresenta parada.
Ao ser chamada com o parâmetro 1, o if da linha 2 tem condição verdadeira.
Então ocorre a chamada a rec(0).
Mas rec(0) não é definido;
assim, ocorrerá a chamada a rec(-1) - e assim sucessivamente.
'''