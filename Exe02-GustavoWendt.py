#02-Escreva um programa para exibir na tela o nome e a categoria de um lutador o programa deve ler em ”string” para o #nome e um número real para o peso.
#Conforme o peso ocorrera  o enquadramento na categoria conforme na tabela
nome=input("Digite o nome do lutador(a): ")
peso=float(input("Digite o peso do lutador(a): "))
if peso <52:
    categoria='inválido'
elif peso >=52 and peso <65:
    categoria='peso pena'
elif peso >=65 and  peso <72:
    categoria='leve'
elif peso >=72 and peso <79:
    categoria='ligeiro'
elif peso >=79 and peso <86:
    categoria='médio'
elif peso >=86 and peso <100:
    categoria='médio pesado'
elif peso >=100:
    categoria='peso pesado'
else:
    print ("Dados fornecidos inválidos")


print("O lutador(a)",nome ,"está na categoria ",categoria )
print("Gustavo Wendt")