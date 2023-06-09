"""
Nome do Programa: PRINT  e FORMAT - Formatar valores dentro da string (igual linguagem C)
Nome do Autor: Renan Lucas da Silva
Data e Hora: 12.02.23 (21h18)

    Descrição:
    Transformando print() do Python em printf() do C.
    Formatando a string dentro de print().
    Usa-se chaves dentro da string para posicionar e o comando format para inserir.
"""
# variáveis
peso = 95
altura = 1.78
idade = 26

# Método 1
print("Peso: {}, Altura: {}, Idade: {}.". format(peso, altura, idade));

    # Esse primeiro estilo se parece com a função printf() da linguagem C, on se posiciona na string e se declara no final.

# Método 2
print(f"Peso: {peso}, Altura: {altura}, Idade: {idade}.");

    # Esse método é mais intuitivo, se declarando no início com a letra 'f'.


# Posicionamento por espaço
print("{:10},{:20}". format(peso, altura));
    # Aqui ele criar um espaço entre o inicio e seu dado, de acordo com a quantidade que você estipulou.

# Controlando decimais, casas a partir da vírgula
print("{:10.4}". format(2/3));
    # ao usar {10.4} determinamos que a saída terá cálculo até 10 casas mas apenas 4 serão usadas.
print("{:11.8}". format(3.141592653589));
    # PI

