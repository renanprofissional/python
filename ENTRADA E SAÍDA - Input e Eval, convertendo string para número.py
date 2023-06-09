"""
Nome do Programa: ENTRADA E SAÍDA - Input e Eval, convertendo string para número
Nome do Autor: Renan Lucas da Silva
Data e Hora: 12.02.23 (20h00)

    Descrição:
    A função de entrada input() entende todo dado digitado como STRING.
    Para receber dado do tipo numério é necessário realizar conversão com eval().
"""


"""EXEMPLO 01"""
# valor em string
valor_string_A = '32'

# conversão para número
eval(valor_string_A)

# saída para mostrar o tipo de dado que é
print((valor_string_A), " = ", (type(valor_string_A)));
    # o valor da variável em aspas está em texto,
    # mas depois ele é convertido em número pelo eval()




"""EXEMPLO 02"""
# jeito simples: um de cada vez
valor = input("Digite um valor: ");
eval(valor)
print("Seu valor é: ", (valor));


# jeito composto: tudo numa só linha
var_input_eval = eval(input('Digite um número ou uma fórmula matemática: '))

print(var_input_eval);
print("O tipo do dado é: ", type(var_input_eval))
print("Ele foi convertido de string no exato momento em que você deu a entrada");
    #Numa mesma linha foi feito o pedido+entrada próprio do input e
    #depois foi feita a conversão em número pelo eval (por ordem dos parênteses).
