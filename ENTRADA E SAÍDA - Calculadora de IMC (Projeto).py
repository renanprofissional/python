"""
Nome do Programa: ENTRADA E SAÍDA - Calculadora de IMC
Nome do Autor: Renan Lucas da Silva
Data e Hora: 12.02.23 (20h48)

    Descrição:
    Uso dos conceitos básicos de variáveis e entradas/saídas
"""


# entrada
peso = eval(input("Digite o seu peso em quilos: "));
altura = (eval(input("Digite a sua altura em centímetros: ")))/100
# fórmula
imc = peso/(altura**2)
# saída
print("Parabéns! Seu IMC é de {:6.4}! Veja abaixo em qual categoria você se encontra:". format(imc));
print("Menor que 18.5 = Magreza");
print("18.5 à 24.9 = Peso normal");
print("25 a 29.9 = Sobrepeso");
print("30 a 34.9 = Obesidade grau 1");
print("35 a 40 = Obesidade grau 2");
print("Maior que 40 = Obesidade grau 3");