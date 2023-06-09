"""
Nome do Programa: FUNÇÃO - Estrutura de decisão para escolha de qual função básica
Nome do Autor: Renan Lucas da Silva
Data e Hora: 18.02.23 (01h06)

    Descrição:
    
"""

escolha = input("Escolha uma opção de função: 1 ou 2\n")
if escolha == "1":
    def func1(x):
        return x + 1
    s = func1(10)

else:
    def func2(x):
        return x + 2
    s = func2(10)

print(s)