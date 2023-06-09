# Docstrings, Documentação de funções

'''
Em Python, é possível definir uma string que serve como documentação de funções definidas pelo desenvolvedor.
Ao chamar o utilitário help() passando como parâmetro a função desejada, essa string é exibida.
O comentário deve ser logo acima da função.
'''

# Determina o n-ésimo termo da sequência de Fibonacci
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

print(help(fibo))