"""
Nome do Programa: BUBBLESORT - Organizar vetor em ordem crescente passo a passo
Nome do Autor: Renan Lucas da Silva
Data e Hora: 02.06.23 (21h15)

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
"""


# FUNÇÃO principal
def bubble_sort(lista):
    
    # QUANTIFICAR, é necessário saber o tamanho da lista pois ela será repetida várias vezes, por isso usa-se 'len' na variavel 'lista' a fim de identificar o número de índices dentro do vetor
    # ou seja, essa linha vai garantir o posicionamento na hora de comparar
    n = len(lista)
    
    
    
    # REPETIR a comparação várias vezes, pois não basta realizar uma iteração de comparação, é necessário comparar várias vezes até que todos estejam organizados; n = número de índices dentro do vetor obtido pelo 'len' - 1 = penúltimo índice que será comparado com o último
    # ou seja, essa linha vai garantir que a iteração de comparação seja feita varias vezes;
    for j in range(n-1):
    

    
    
    # BLOCO de código que irá fazer comparações entre elementos sucessivos
    
        # PERCORRER, vai percorrer todos os indices do vetor até o penultimo, pois dali mesmo será feita a comparação com o ultimo posicionado (n = ultimo, n-1 = até o penultimo)
        # ou seja, essa linha percorrerá todos os elementos do vetor
        for i in range(n-1):
        
        
            # COMPARAR, verificar se quem está na posição 'i' da lista ('i' = elemento em iteração) é maior do que quem está na posição 'i+1' (seu sucessor consecutivo, que está ao seu lado, o índice seguinte = i+1)
            # ou seja, essa linha vai verificar se o índice antecessor é maior que o sucessor
            if lista[i] > lista[i+1]:
            
                # TROCAR, mudar as posições de cada elemento trocando seus valores; python permite trocar valores entre variáveis de forma direta e simples, sem criar uma variável auxiliar
                # ou seja, essa linha vai trocar os valores de lugar caso o antecessor de fato seja maior que o sucessor
                lista[i], lista[i+1] = lista [i+1], lista[i]
                # i virou i+1 e vice-versa, i+1 virou i, ou seja, inverteram-se os valores e consequentemente as posições /índices
            
                #REPETIR várias vezes, ao invés de percorrer todos os elementos uma vez só, por isso é necessário repetir 'n-1' vezes a iteração
                # portanto, é necessário colocar todo esse bloco de iteração dentro de outro bloco de iteração; irá repetir a repetição, isto é, executar o laço de iteração várias vezes



# LISTA que será aplicado o método bubblesort
lista_baguncada = [45,22,67,11,6,987,123,1]

# ANTES E DEPOIS da chamada da função para mostrar os resultados
print("\nLISTA ANTES DO BUBBLESORT: ", lista_baguncada)
bubble_sort(lista_baguncada)
print("\nLISTA DEPOIS DO BUBBLESORT: ", lista_baguncada)

