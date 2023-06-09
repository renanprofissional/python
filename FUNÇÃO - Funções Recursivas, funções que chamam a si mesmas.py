"""
Nome do Programa: FUNÇÃO - Funções Recursivas, funções que chamam a si mesmas
Nome do Autor: Renan Lucas da Silva
Data e Hora: 21.02.23 (04h05)

    Descrição:
    Funções recursivas
    Uma função recursiva é aquela que chama a si mesma.
    Tem uma chamada com seu próprio nome dentro de si;
    Essa execução será repetida indefinidamente até que haja algum erro por falta de memória.
    Veja o exemplo da função regressiva() 
    
"""


# INFINITA
def regressiva(x):
   print(x)
   regressiva(x - 1)

regressiva(2)

# Na chamada 'regressiva(2)' o valor 2 é exibido na tela;
# Uma nova chamada acontece dentro da própria função, subtraindo 1 (2-1=1);
# Essa nova chamada inicia a função com valor 1, printando e depois sendo chamado e subtraído de novo (1-1=0);
# Após a chamada e a subtração, é realizado um novo print e uma nova chamada+subtração = -1;
# A função tende assim perpetuamente: chamar-se, printar-se e chamar-se novamente se subtraindo;


''' COM FIM: repetirá até que X seja = a -300
def regressiva(x):
   print(x)
   if x > (-300):
       regressiva(x - 1)

regressiva(10)'''