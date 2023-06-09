"""
Nome do Programa:  FUNÇÃO - Tipos de Função (Simples, com Parâmetro, Decisão, Repetição, etc.)
Nome do Autor: Renan Lucas da Silva
Data e Hora: 19.02.23 (22h20)

    Descrição:
    
"""

# Chamada Simples
print("***EXECUTANDO UMA FUNÇÃO SIMPLES***")
def funcao_simples ():
    print("uma string de texto simples.")
funcao_simples()

# Função recebendo parâmetro
print("\n\n\n***FUNÇÃO SIMPLES COM PARÂMETRO***")
def funcao_simples_p (parametro_recebido):
    resultado_funcao_simples = parametro_recebido+5
    print(resultado_funcao_simples)
valor_parametro_simples = eval(input("Digite um valor para mandar para dentro da função: "))
funcao_simples_p (valor_parametro_simples)


# Uma mesma Função em estilo diferente por Decisão/condicional
print("\n\n\n***DETERMINAR COMO UMA MESMA FUNÇÃO VAI SER***")
decisao_estilo = eval(input("Digite '1' para executar a função no primeiro estilo ou '2' para executa-la no segundo estilo\n.\n"))
if decisao_estilo == 1:
    def funcao_cond ():
        print("Você_acabou_de_executar_a_função_NO_ESTILO_número_um.")
else:
    def funcao_cond ():
        print("Você acabou de executar a função NO ESTILO número dois.")
funcao_cond()

# Escolher entre Duas funções diferentes por decisão/condicional
print("\n\n\n***ESCOLHER QUAL ENTRE DUAS FUNÇÕES DIFERENTES SERÃO EXECUTADAS***")
def funcao_numero1 ():
    print("Esta é a função PRIMEIRA, própria e específica.")
def funcao_numero2 ():
    print("Esta é a função SEGUNDA, própria e específica.")
decisao_entre2funcoes = input("Digite '1' para escolher especificamente a função numero 1 ou digite '2' para escolher a funcao numero 2.\n")
if decisao_entre2funcoes == 1:
    funcao_numero1 ()
else:
    funcao_numero2 ()

# Loop executando a função
print("\n\n\n***PARA CADA DIGITO, EXECUTE A FUNÇÃO***")
resultado_for = 0
def funcao_dobra_for(x):
    x = x*2
    print(x)
for contador in range(10):
    resultado_for = 10*contador #multiplica por 10
    funcao_dobra_for(resultado_for) #dobra o valor e printa

print("\n\n\n***ENQUANTO X FOR TAL VALOR, EXECUTE A FUNÇÃO***")
resultado_while = 0
contador_while = 0
def funcao_potenciacao_while (x):
    x = x**2
    print("O quadrado desse número é: {}.". format(x))
while resultado_while < 10:
    resultado_while = 1+contador_while
    contador_while += 1
    print(resultado_while)
    funcao_potenciacao_while (resultado_while)
