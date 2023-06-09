"""
Nome do Programa: SEQUÊNCIAS - Geração de lista, tupla e range
Nome do Autor: Renan Lucas da Silva
Data e Hora: 10.02.23 (20h25)

    Descrição:
    Criar variáveis em sequência, determinar quantos itens possui e então escrevê-las.
"""

#variável com itens em sequência
a = ['U']+['RN']
b = ['4']*4

#saída da quantidade de itens por série sequência
print(len(a));
print(len(b));

#saída de cada item
print (a);
print (b);

"""
EXPLICAÇÃO:
    a = ['U']+['RN']
    O operador + soma números e junta sequências.
    Assim, a variável 'a' passa a ser composta por:
        ‘UF’ e ‘RN’
    Logo, a chamada len(a) retorna o tamanho 2, número de elementos de 'a'.
    
    b = ['4']*4
    De forma semelhante, o operador * multiplica números e junção de cópias para tipos sequenciais.
    A variável 'b' passa a ter quatro cópias:
        '4', '4', '4', '4'
    Depois a chamada len(b) retorna a quantidade de itens da variável 'b' = 4.
"""