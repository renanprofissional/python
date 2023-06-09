"""
Nome do Programa: IMPORT - Referenciação, no início ou toda vez que for usar uma função
Nome do Autor: Renan Lucas da Silva
Data e Hora: 08.06.23 (05h00)

    DESCRIÇÃO:
        Pode-se usar funções de uma biblioteca referenciando na hora
        Ou pode-se referenciar uma unica vez no começa, não precisando mais depois
        
        import math
        x = math.sqrt(4)
        
        ou
        
        from math import sqrt
        x = sqrt(4)
"""
# importar e declarar toda vez que for usar a função
import math
x = math.sqrt(4)
print(x)

# importar e declarar no inicio, não precisando referenciar depois
from math import sin, cos, tan
a = sin(45)
b = cos(45)
c = tan(45)
print(a,b,c)