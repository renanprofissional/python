"""
Nome do Programa: Calculadora de IMC com 3 opções de saída
Nome do Autor: Renan Lucas da Silva
Data e Hora: 25.03.23 (10h35)

"""

# título de apresentação
print ("============================================")
print ("BEM VINDO A CALCULADORA DE MASSA CORPORAL!")
print ("============================================")

# entrada de dados e cálculos
altura = eval(input ("\n\n\nDigite a sua altura em centímetros: "))
peso = eval(input ("Digite o seu peso em quilogramas, sem adição de gramas após a vírgula: "))
imc = peso/((altura/100)**2)

# saída de dados e avaliação
if imc < 18.5:
    print ("Seu IMC resultou em: ", imc)
    print ("Segundo o índice, isso é considerado abaixo do ideal e portanto, não é saudável. Procure corrigir sua alimentação e praticar atividades físicas.")

elif imc > 25:
    print ("Seu IMC resultou em: ", imc)
    print ("Segundo o índice, você está em sobrepeso, considerado então como não sendo saudável. Procure praticar atividades físicas e corrigir sua alimentação para sua saúde não ser prejudicada.")
    
else:
    print ("Seu IMC resultou em: ", imc)
    print ("Segundo o índice, isso é considerado o ideal e portanto, saudável. Ainda assim, procure praticar atividades físicas e se alimentar bem, pois a faixa de peso ideal não garante saúde por si só.")

"""
COMENTÁRIOS:
Eu encontrei dificuldades com estrutura de decisão if.
Tentei escrever elif, mas esse não é um comando válido.
Tentei com uma série de else, tambem nao funcionou.
Ao combinar elif com else, a sintaxe aceitou.
A sintaxe não aceitou dois operadores relacionais numa mesma linha, combinados com um booleano:
    Exemplo elif >= 18.5 and <= 25:
Para resolver o problema, foi feito relacionais somente para 2 opções (< 18.5 e > 25),
    enquanto que o terceiro que ficaria no meio, simplesmente não foi adicionado nada.
"""