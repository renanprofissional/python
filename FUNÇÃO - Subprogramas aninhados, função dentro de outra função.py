"""
Nome do Programa: FUNÇÃO - Subprogramas aninhados, função dentro de outra função
Nome do Autor: Renan Lucas da Silva
Data e Hora: 20.02.23 (04h54)

    Descrição:
    Em Python (e na maioria das linguagens funcionais), é permitido aninhar subprogramas.
    Contudo, as linguagens C e C++ não permitem essa prática.
    A função taximetro() tem, dentro de sua definição, a definição de outra função denominada calculaMult().
    A função calculaMult() é chamada, e o seu retorno é armazenado na variável multiplicador.
    
"""
# uma função dentro de outra função
def taximetro(distancia):
    def calculaMult():
        if distancia < 5:
            return 1.2
        else:
            return 1

    multiplicador = calculaMult()
    largada = 3
    km_rodado = 2
    valor = (largada + distancia * km_rodado) * multiplicador
    return valor


dist = eval(input("Entre com a distancia a ser percorrida em km: \n"))
pagamento = taximetro(dist)
print(f'O valor a pagar é R$ {pagamento}')