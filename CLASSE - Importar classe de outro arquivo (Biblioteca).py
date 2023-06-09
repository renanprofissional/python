"""
Nome do Programa: CLASSE - Definição e criação de uma classe
Nome do Autor: Renan Lucas da Silva
Data e Hora: 24.02.23 (12h00)

    Descrição:
    Num arquivo X importar classe de um arquivo Y.
    Funciona como uma biblioteca
    Comando 'from' designa o arquivo de origem
    Comando 'import' designa a classe desejada
    Utiliza-se os mesmos comandos de como se estivessem juntos:
        variável = classe (parâmetros)
        variável.função (parâmetros)

"""

# importar classe de outro arquivo

from classes01 import Vendedor
    # from 'arquivo' import 'classe'
    
vendedor_um = Vendedor ("Fulano")
    # variável = classe (parâmetros)
vendedor_um.vendeu (1000)
    # variável.função (parâmetros)
vendedor_um.bateu_meta(700)
    # # variável.função (parâmetros)

# é possível utilizar uma classe de outro arquivo/local
# é necessário que o arquivo onde a classe esteja, seja do mesmo local que este arquivo aqui
# é necessário que seja um arquivo de nome curto e singula, sem espaço, etc.