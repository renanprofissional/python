# PASS - Criação de uma exceção, decisão e repetição

# o comando "pass" tem função semelhante ao "continue": ele pula uma ação, cria uma exceção.
# algoritmo para printar somente numeros impares
for numero in range(1,11):
    if numero %2 == 0:
        pass
    else:
        print(numero)
print("Ciclo encerrado.");

'''EXPLICAÇÃO: Esse algorítmo usou o loop em range para printar números de 1 a 10.
Para printar somente os números ímpares, a lógica foi: números pares quando divididos por 2, formam inteiros perfeitos,
enquanto que números ímpares dividos por 2 sempre são "X,5", isto é, sobram uma casa decimal.
Logo, todo número que não sobrar uma casa decimal, será 'passada' = pass, não será printada.
Será printado somente números com algum resto (%), ou seja, números ímpares.'''
