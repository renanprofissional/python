"""
Nome do Programa: ENTRADA - Strip, limpando os espaços que o usuário digita
Nome do Autor: Renan Lucas da Silva
Data e Hora: 08.06.23 (07h06)

    Descrição:
    Quando usuário faz uma entrada de dados
    pode vir espaço antes ou depois do nome
    Limpa-se esses caracteres desnecessário com STRIP
    
"""
# aplicação direta da função STRIP já na entrada dos dados
nome_cadastro = str(input("Digite o seu nome completo: ")).strip()
print("O seu nome é: {}.".format(nome_cadastro))




# para verificar o processo passo a passo, faz-se agora um ANTES e  DEPOIS

# entrada de palavra com espaços antes e depois de si
palavra_antes = str(input("\n\n\nDigite espaços ANTES  e DEPOIS de uma palavra: "))

# contagem dos caracteres totais, letras+espaços
antes_quant = len(palavra_antes)
print("\nA quantidade de caracteres identificados pelo sistema foi de: {}".format(antes_quant))

# aplicação da função STRIP na palavra cheia de espaços
palavra_depois = palavra_antes.strip()

# contagem da palavra após a aplicação da função STRIP
depois_quant = len(palavra_depois)
print("\nA quantidade de caracteres identificados após a função STRIP foi de: {}".format(depois_quant))