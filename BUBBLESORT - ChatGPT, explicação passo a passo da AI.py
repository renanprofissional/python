"""
Nome do Programa: BUBBLESORT - ChatGPT, explicação passo a passo da AI
Nome do Autor: Renan Lucas da Silva
Data e Hora: 02.06.23 (22h10)

    Descrição:
    Bubblesort é uma estrutura de dados que visa organizar dados para determinada posição no vetor
    Vão-se comparando elemento com elemento dentro do vetor
    Neste caso, a organização é feita de maneira crescente = se A for maior que B, ambos trocam de lugar e A passa pra frente
    Os maiores vão indo pra frente e os menores vão pra trás
    Posiciona-se elementos do menor ao maior, não importanto o que quão bagunçados estivessem
    É relativamente complexo, por isso demora em execução
    
    Passo-a-passo:
        1. Têm-se um array com valores
        2. Cria-se uma repetição para percorrer todos os valores
        3. Cria-se uma condicional para comparar se A é maior que B
        4. Cria-se um código de troca de valores/posição caso A seja maior que B
        5. Esse procedimento será realizado até o último elemento graças a repetição
        6. Cria-se outra repetição englobando a iteração primeira, para garantir que o ciclo se repita varias vezes até todos os elementos estarem organizados
        
    DIFERENÇAS:
    Nessa versão do ChatGPT, o algorítmo não compara os valores grandes já passados pra frente
    aqui se foca apenas no valores menores que ainda estão desorganizados
    A diferença está na linha 48
"""


# essa linha define a função bubblesort, que vai receber uma série valores em 'numbers'
def bubble_sort(numbers):
    
    # essa linha vê quantos itens há em 'numbers', para se orientar nas repetições a fim de controlar as iterações
     n = len(numbers)
     
     # começa uma repetição que irá iterar n-1 (até a penúltima posição)
     for i in range(n-1):
         
         # uma variável com valor 'False' para checar se alguma troca foi feita dentro da repetição
         swapped = False
         
         # essa linha começa uma repetição interna que irá comparar e trocar dois elementos paralelos;
         # a range do loop vai de 0 até n-i-1 porque a cada iteração do loop maior (de fora desse), o maior elemento já está no fim da lista, logo, não há necessidade dele ser comparado de novo.
         # n = total de elementos no vetor; i = etapa da iteração; -1 = até o penúltimo
         for j in range (n-i-1):
             
             # aqui se compara o objeto de iteração atual com seu sucessor, verificando se é maior que ele
             # j = valor em iteração; j+1 = seu sucessor seguinte
             if numbers[j] > numbers[j+1]:
                 
                 # aqui serão trocados de posição, o maior vai pro lugar da frente e o menor vai pro lugar de trás
                 numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                 
                 # aqui a variavel 'swapped' terá seu valor mudado para 'True' pois houve troca ed lugares entre valores na iteração
                 swapped = True
            
            
            # caso os números comparados não troquem e não haja mais nenhuma troca posterior, os ciclos terminam
         if not swapped:
            break


unsorted_list = [45,22,67,11,6,987,123,1]
print(unsorted_list)
bubble_sort(unsorted_list)
print(unsorted_list)