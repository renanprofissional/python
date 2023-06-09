"""
Nome do Programa: VARIÁVEL - Troca de Variáveis
Nome do Autor: Renan Lucas da Silva
Data e Hora: 10.02.23 (21h25)

    Descrição:
    Em C e Java, seria necessário criar uma terceira variável para trocar e valor de duas variáveis.
    Python dispensa isso com o uso de atribuição múltipla.
    Segue abaixo as duas maneiras, variável auxiliar e atribuição múltipla.
"""

# variáveis
a = 1
b = 2
x = 12
y = 20

# troca de variáveis usando variável auxiliar ‘temp’
# C e Java
temp = a
a = b
b = temp
print(f"O valor da variável a é: {a}")
print(f"O valor da variável b é: {b}")

# troca de variáveis através de atribuição múltipla
# Python
x, y = y, x
print(f"O valor da variável x é: {x}")
print(f"O valor da variável y é: {y}")

#inverteu-se; com uma única equação é possível re-atribuir seus valores