"""
Nome do Programa: LEN - Len, contagem de valores
Nome do Autor: Renan Lucas da Silva
Data e Hora: 08.06.23 (07h21)

    Descrição:
    A função "len()" conta a quantidade de elementos
    Funciona dentro de uma string, mas não de números
    
"""

# entrada de texto do usuário
palavra = str(input("Digite uma palavra: "))

# a função 'len()' irá contar quantos elementos existem e guardar na variavel 'palavra_quant'
palavra_quant = len(palavra)

# a quantidade de elementos, dada pela função len(), na saída formatada
print("A quantidade de elementos nessa palavra é de: {}".format(palavra_quant))


# com numero não funciona
numero = int(input("\n\n\nDigite um número qualquer: "))
numero_quant = len(numero)
print("A quantidade de elementos no numero é de: {}.".format(numero_quant))