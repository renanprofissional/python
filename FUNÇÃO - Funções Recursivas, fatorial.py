"""
Nome do Programa: FUNÇÃO - Funções Recursivas, fatorial
Nome do Autor: Renan Lucas da Silva
Data e Hora: 21.02.23 (05h10)

    Descrição:
    Funções recursivas
    Uma função recursiva é aquela que chama a si mesma.
    Tem uma chamada com seu próprio nome dentro de si;
    Essa execução será repetida indefinidamente até que haja algum erro por falta de memória.
    Nesse caso visa aplicar o conceito a FATORIAIS.
    
"""

# função recursiva fatorial

def fatorial(n):
    if n == 0 or n == 1:
         return 1
    else:
         return n*fatorial(n-1)
        


# fatorial de forma não recursiva
def fatoria2(n):
    fat = 1
    if n == 0 or n == 1:
        return fat
    else:
        for x in range(2, n + 1):
               fat = fat*x
        return fat