#No Senailândia mulheres e homens podem servir o exército do país.
#O serviço é opcional e é muito comum que as pessoas se apresentem para o serviço em algum momento da #vida. Existe uma única restrição para o ingresso que é a idade da pessoa:
#Para mulheres a idade aceita é entre 21 e 34 anos.
#Pra homens a idade aceita é entre 18 e 39 anos.
#Escreva um programa que leia três dados de entrada: O nome da pessoa, idade e sexo, e informe se a #pessoa vai poder servir ou não. Obs: Para o sexo deve ser lido apenas um caractere que pode “f” ou #“F” ou “n” “N”. Qualquer coisa diferente deve ser informado “Dado inválido”.
nome = input("Qual seu nome: ")
genero = input("Qual seu sexo (F, f para feminino ou M, m para masculino:")
idade = int(input("Qual sua idade?: "))
genero2=genero.title()
if genero2 == 'F' :
      if idade >=21 and idade <=34:
         print("Você está altorizado ao SERVIÇO MILITAR ")
         print("Gustavo Wendt")
      else:
           print("Você não está altorizado ao SERVIÇO MILITAR ")
           print("Gustavo Wendt")
elif genero2 =='M':
     if idade >=18 and idade <39:
          print("Você está altorizado ao SERVIÇO MILITAR ")
          print("Gustavo Wendt")
     else:
        print("Você não está altorizado ao SERVIÇO MILITAR ")
        print("Gustavo Wendt")