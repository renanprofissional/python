# DECISÃO - Elif, duas condicionais em sequência, If e Elif, depois o Else

objetivo = input("Qual o seu objetivo dentro da academia?\n Voce quer 'ganhar massa' ou 'perder peso'?\n");

if objetivo == "ganhar massa":
    print("\nVocê precisa focar em treinos de hipertrofia combinados com uma dieta hipercalórica.");
elif objetivo == "perder peso":
    print("\nVocê precisa focar em treinos aeróbicos combinados com uma dieta restritiva.");
else:
    print("\nDesculpe, não conseguimos entender o que você escreveu. Tente novamente mais tarde.");

print("\nNós da EQUIPE FERREIROS desejamos a você uma excelente saúde e qualidade de vida!");

# é possível adicionar diversas elif's