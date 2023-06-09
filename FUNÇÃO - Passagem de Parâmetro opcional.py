"""
Nome do Programa: FUNÇÃO - Passagem de Parâmetro opcional
Nome do Autor: Renan Lucas da Silva
Data e Hora: 24.02.23 (08h35)

    Descrição:
    Toda passagem de parâmetro é obrigatória para uma função que trabalha com parâmetros específicos.
    Todavia, é possivel criar um jeito para fazer com que a função trabalhe com menos parâmetros do que foi programada para trabalhar.
    Através do uso subentendido dentro do seu cabeçalho.
    
"""

# Passagem de Parâmetro opcional

# passagem comum
def somar1 (a, b, c):
    s = a+b+c
    return s

print(somar1(3,5,8))

"""Nessa situação, é obrigatório a passagem de 3 parâmetros
da chamada de função para dentro da função (a, b, c);
Se for passado apenas 2 parametros dará erro.

"TypeError: somar1() missing 1 required positional argument: 'c'"
"""

# passagem opcional
def somar2 (a=0, b=0, c=0):
    s=a+b+c
    return s

print(somar2(2,3))


"""
Já neste caso, caso não seja passado algum parâmetro
da chamada para dentro da função, a função entenderá como "0" (zero),
prosseguindo com o cálculo adiante, não incorrendo em TypeError.
"""