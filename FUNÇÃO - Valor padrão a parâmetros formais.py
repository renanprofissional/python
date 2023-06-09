"""
Nome do Programa: FUNÇÃO - Valor padrão a parâmetros formais
Nome do Autor: Renan Lucas da Silva
Data e Hora: 18.02.23 (01h06)

    Descrição:
    
"""

def taximetro(distancia, multiplicador=1): # parametro não declarado = valor padrão
    largada = 3
    km_rodado = 2 #eval(input("Quantos quilometros voce rodou?"))
    valor = (largada + distancia * 
    km_rodado) * multiplicador
    #print(largada)
    #print(distancia)
    #print(km_rodado)
    #print(multiplicador)
    return valor


pagamento = taximetro(3.5) #aqui se encontra o valor padrão do parâmetro 'distancia'
print(pagamento)