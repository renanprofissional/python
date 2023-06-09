"""
Nome do Programa: CLASSE - Definição e criação de uma classe
Nome do Autor: Renan Lucas da Silva
Data e Hora: 24.02.23 (11h25)

    Descrição:
   Definição de classe e seu uso.
   Criação da classe com comando 'class'
   Primeira função de identidade com '__init__' + parâmetros que a definirão
   Funções com parâmetros 'self' para indicar que pertencem a uma classe
   Variável específica recebendo valor ao se vincular a uma classe: 'vendedor1 = Vendedor ("Lira")'
   Execução das funções da classe para o caso de cada vendedor.
    
"""

# Classes em Python
# Uma forma de desenvolver códigos, mais complexos, que nao vao ser um unico arquivo num unuico comando











# situação normal, simples, comum
vendedorr = "lira"
vendass = 1000
metaa = 500

if vendass >= metaa:
    print("Bateu a meta.")
else:
    print("Não bateu a meta.")

# caso houvesse um novo vendedor, seria necessário criar todo esse bloco de código dedicado à uma nova variável 'vendedor'.
# tudo reescrito para a variável vendedor2
# várias espécies de um mesmo gênero








# CRIANDO UMA CLASSE
# criar uma classe que vai gerir todas as informações que ela, o objeto, terá
# objeto =  classe = vendedor

class Vendedor ():
    def __init__(self, nome):
        # a primeira coisa ao criar uma classe é gerar uma função "init" = ela cria o Vendedor
        # '__init__' = função principal
        # o "self" fará parte de todas as funções dentro da classe, referenciam a classe
        # do lado deste self é gerado as informações necessárias para definir o Vendedor, no caso, 'nome'
        
        self.nome = nome
        self.vendas = 0
        # o 'self' refletirá o objeto da classe, no caso, 'Vendedor'
        # o 'nome' adiante do self.nome reflete o parâmetro dado no cabeçalho da função
        
    def vendeu (self, vendas):
        self.vendas = vendas
        # nesse mesmo caso, 'self.vendas' reflete a classe 'Vendedor' enquanto que 'vendas' é o parâmetro recebido
    
    def bateu_meta (self, meta):
        if self.vendas > meta:
            print(self.nome, " Bateu a meta.")
        else:
            print(self.nome, " Não bateu a meta.")

# agora é possivel utilizar todo esse bloco de código padronizado para todas as situações seguintes, sem precisar reescrever



# utilizando a classe numa situação

vendedor1 = Vendedor("Lira")
# criou-se um vendedor específico e passou dentro da chamada da classe toda informação necessária do "__init__", neste caso, 'nome'

print(vendedor1.nome)
# aqui confirma: a variável 'vendedor1' recebeu o valor literal 'Lira' que veio do parâmetro 'nome' da classe 'Vendedor'

vendedor1.vendeu (500)
    # aqui é transmitido a informação para a função de 'venda', para armazenar o valor de vendas
vendedor1.bateu_meta(400)
    # aqui é transmitida a informação para a função de 'bateu_meta', para ver se o individuo bateu a meta
    

# segunda situação
vendedor2 = Vendedor("Renan")
print(vendedor2.nome)
vendedor2.vendeu(300)
vendedor2.bateu_meta(100)



'''
OU PODE-SE UTILIZAR ENTRADAS DADAS PELO CLIENTE:

vendedor1.vendeu (eval(input("Quanto o vendedor 1 vendeu? ")))
vendedor1.bateu_meta(eval(input("Qual foi a meta estipulada? ")))
'''