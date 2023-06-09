"""
Nome do Programa: ENTRADA E SAÍDA - Diferentes tipos de entradas e saídas
Nome do Autor: Renan Lucas da Silva
Data e Hora: 10.02.23 (22h20)

    Descrição:
    Diferentes tipo de entrada e saída de dados.
"""

#Entrada e Saída de Dados

#saída com print
print("exemplo de texto");

'''
PYTHON X C
Em C, o printf() precisa de '\n' para pular de linha, em python isso é automático.
Em C, você precisa indicar o formato que a variável será expressa: %s (string), %d (inteiro), %f (decimal), em python isso é automático.
'''
#saída de string direta
print ('string de texto')

#saída de variáveis
var_caractere = 'A'
print(var_caractere)
var_inteiro = 7
print(var_inteiro)
var_decimal = 3.1416
print(var_decimal)

#saída de sequências
seq_A = [0, 2, 4, 6, 8, 10]
print(seq_A)

#saida e entrada de dados
var_nome = input("Digite seu nome: ")
print(var_nome)

'''
Em C, usa-se printf(); e scanf(); para fazer o pedido de dados ao usuário e permitir ele digitar.
Em Python, apenas input faz as duas coisas, pedido e entrada ao mesmo tempo.
Após isso, basta a saída do dado do usuário.

Em C:
    char nome [20];
    printf ("Digite o seu nome: ");
    scanf ("%s", &nome);
    printf ("Seu nome é %s", nome);
Em Python:
    nome = input("Digite seu nome: ")
    print(nome)

<PS> input() só reconhece como string de texto.
'''

#convertendo string em número com eval()
valor_string_A = '32'
eval(valor_string_A)
print(valor_string_A);
    # o valor da variável em aspas está em texto,
    # mas depois ele é convertido em número pelo eval()'''

'''combinar com input(): trisformar a string de input em número através do eval()'''
var_input_eval = eval(input('Digite um número ou uma fórmula matemática: '))
print(var_input_eval);
    # Numa mesma linha foi feito o pedido+entrada próprio do input e
    # depois foi feita a conversão em número pelo eval (por ordem dos parênteses).