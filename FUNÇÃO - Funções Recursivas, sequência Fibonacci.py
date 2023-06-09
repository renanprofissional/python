"""
Nome do Programa: FUNÇÃO - Funções Recursivas, sequência Fibonacci
Nome do Autor: Renan Lucas da Silva
Data e Hora: 21.02.23 (05h15)

    Descrição:
    A sequência de Fibonacci é: 1, 1, 2, 3, 5, 8, 13, 21...
    Os dois primeiros termos são 1; a partir do 3º termo, cada termo é a soma dos dois anteriores.
    Uma função recursiva para gerar uma sequência Fibonacci.
"""

# título
print("-"*40)
print("SEQUÊNCIA FIBONACCI COM FUNÇÃO RECURSIVA")
print("-"*40, "\n\n")

# sequência fibonacci
def fibo(n):
    if n == 1 or n == 2: #condição de parada
        return 1
    
    else:
        return fibo(n - 1) + fibo(n - 2) #chamada para calcular os dois termos anteriores da sequência
        
fibo(20)