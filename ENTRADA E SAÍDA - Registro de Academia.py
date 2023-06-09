"""
Nome do Programa: ENTRADA E SAÍDA - Registro de Academia
Nome do Autor: Renan Lucas da Silva
Data e Hora: 15.02.23 (01h06)

    Descrição:
    Uso dos conceitos básicos de variáveis e entradas/saídas.
"""

# ficha de academia

#entrada de dados do usuário
print("========= BEM VINDO A ACADEMIA! =========");
print("FICHA DE INSCRIÇÃO");
nome = input("Nome: ");
idade = eval(input("Idade: "));
altura = (eval(input("Altura (em centímetros): ")))/100;
peso = float(eval(input("Peso: ")));
tempo_treino = eval(input("Tempo de Treino (em anos): "));
objetivo = input('Digite "A" para Ganho de Peso ou "B" para Perder Peso: ');

# confirmação de dados do usuário
print("          CONFIRA OS SEUS DADOS");
print("Nome: {}.". format(nome));
print("Idade: {} anos.". format (idade));
print("Altura: {}m.". format(altura));
print("Peso: {:8.5}kg.". format(peso));
print("Anos de Treino: {} ano(s).". format(tempo_treino));
print("Objetivo de Treino (A ou B): {}.". format(objetivo));
confirmacao = input("ATENÇÃO: Os dados acima estão corretos? SIM/NÃO: ");

# cálculos a partir dos dados do usuário (erro no range)
print("          RELATÓRIO");

# range
# print(("Foi fornecido um total de {}". format(range(1,8))), (" dados de indivíduo."));

lista_dados = nome, idade, altura, peso, tempo_treino, objetivo
print("Dos quais são: ", lista_dados);
imc = peso/(altura**2)
print("Seu IMC é de {:5.4}. Pessoas saudáveis tender a variar entre 18.5 à 25 pontos.". format(imc));
idade_objetivo = idade+3
print("Você pode atingir seu tão sonhado objetivo caso mantenha o foco até atingir {} anos de idade!". format(idade_objetivo));
