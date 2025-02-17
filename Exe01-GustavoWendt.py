#01-Escreva um programa que forneça o tipo de aplicação financeira a um investidor a partir de dois dados obtidos:  O grau de aceitação de risco e o valor a ser investido.
#O grau de aceitação de risco deve ser lido no teclado na forma BX para baixo ou AL se for fornecido algo diferente disso o programa deve mostrar uma mensagem de que foi fornecido dados invalídos para o valor deve ser um número Real
#Aceitação de risco valor<1000 valor >=
#Baixo(Bx)     poupança      renda Fixa
#lto(Al)        Bitcoins          Ações
risco=input("Qual o nível de rísco aceitavel (Bx- baixo rísco,AL para alto RISCO: ")
valor=float(input("Qual o valor que deseja investir?: "))
if risco=='Bx'and valor<1000:
        print("Recomendação de investivento é poupança")
        print("Gustavo Wendt")
elif  risco == 'Bx' and valor >=1000:
   print("Recomendação de investivento é renda fixa")
   print("Gustavo Wendt")
elif risco =='Al'and valor <1000:
  print("Recomendação de investivento é Bit coin")
  print("Gustavo Wendt")
elif  risco == 'Al' and valor >=1000:
    print("Recomendação de investivento é ações")
    print("Gustavo Wendt") 
else:
    print("Os dados fornecidos estão incorretos")
    print("Gustavo Wendt")   
    
