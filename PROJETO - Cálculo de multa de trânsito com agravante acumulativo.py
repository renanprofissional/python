"""
Nome do Programa: PROJETO - Cálculo de multa de trânsito com agravante acumulativo
Nome do Autor: Renan Lucas da Silva
Data e Hora: 17.02.23 (03h16)

    Descrição:
    Aplicação dos conceitos de decisão (if-else) e repetição (for-range).
    Identificar se o veículo ultrapassou a velocidade permitida, calcular o agravante acumulativa e dar a multa final.
"""

velocidade = eval(input("Qual era a velocidade do veículo na VIA ESCOLAR em HORÁRIO DE TRÂNSITO ESTUDANTIL?\n"));
excedente = velocidade - 40
multiplicador = 0
multa = 0

if excedente <= 0:
    excedente = 0
else:
    excedente = excedente + 1                    # adicional para o range não deixar de calcular o último dígito por ter começado do zero (5 = 0, 1, 2, 3, 4).
    for multiplicador in range(excedente):
        acumulacao = 2*multiplicador
        print(acumulacao)
        multa = multa + acumulacao
    multa = multa + 50                           # piso inicial adicionado após o cálculo acumulativo
    
        # CALCULO - Cada quilometro excedente é contabilizado um multiplicador, e pra cada multiplicador é multiplicado por 5.
        # Depois que os contadores são individualmente multiplicados, eles são somados para mostrar a multa total.
        # Exemplo: 45km - limite de 40 = 5km excedentes; (1*2+2*2+3*2+4*2+5*2) + 50 = 80
        # A contagem é individual e cumulativa, é por cada dígito excedente, ao invés de ser (5*2) + 50 = 10 diretamente.


if excedente == 0:
    print("\nO veículo andou dentro dos limites de velocidade.");
    print("Não será aplicado nenhuma multa.");
else:
    print("\nO veículo ultrapassou os limites de velocidade.");
    print("Será aplicada uma multa no valor de {} reais.". format(multa));

print("Muito obrigado por utilizar a calculadora de multa agravante em vias escolares.");