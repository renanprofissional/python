"""
Nome do Programa: REPETIÇÃO - For com RANGE composta por início e fim
Nome do Autor: Renan Lucas da Silva
Data e Hora: 17.02.23 (03h22)

    Descrição:
    Entrada de dado do usuário por quantos números ele deseja contar.
    Do número 1 até o número que ele deu entrada.
"""

quant = eval(input("Quantos numeros tu quer contar?\n"));
for cont in range(1,quant+1):
    print(cont);