#Uma empresa financeira concede empréstimos a pessoas físicas quando o valor da parcela é menor que 8% que o salário da #pessoa.
#Escreva um programa que leia dois números reais: O valor do salário e o valor da parcela e informe se o empréstimo será #concedido ou não.
salario=float(input("Digite quanto você ganha por mês: "))
parcela=float(input("Qual o valor da parcela?: "))
porcentagem = parcela/salario
if porcentagem <0.08:
  print("empréstimo CONCEDIDO! ")
  print("Gustavo Wendt")
else:
  print("empréstimo NEGADO! ")
  print("Gustavo Wendt")