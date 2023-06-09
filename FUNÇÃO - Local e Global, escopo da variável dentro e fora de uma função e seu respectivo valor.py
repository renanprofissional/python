"""
Nome do Programa: FUNÇÃO - Local e Global, escopo da variável dentro e fora de uma função e seu respectivo valor
Nome do Autor: Renan Lucas da Silva
Data e Hora: 20.02.23 (04h30)

    Descrição:
    Existem dois escopos: global e local.
    Uma variável global pode ser usada dentro de uma função sem declaração prévia por parâmetro.
    Essa variável global terá valor e alterações apenas locais.
    Para que as alterações sejam feitas globalmente, é necessário especificar tal coisa.
    


"""

# variáveis globais
var_global1 = "Palavra um."
var_global2 = "Palavra dois."

# função
def funcao ():
    #variáveis locais
    var_local1 = 10
    var_local2 = 20
    print(var_local1)
    print(var_local2)
        
    # alteração e print das variáveis globais
    var_global1 = "Alteração local na variável global 1."
    var_global2 = "Alteração local na variável global 2."
    print(var_global1)
    print(var_global2)

# print das variáveis globais originais
print(var_global1)
print(var_global2)

# chamada da função
funcao()

# print das variáveis globais após execução da função
print(var_global1)
print(var_global2)