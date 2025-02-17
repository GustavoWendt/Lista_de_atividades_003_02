#no comércio o conceito de margem bruta é uma porcentagem que é aplicada ao preço de custo para ser #Uma loja tem como política comercial aplicar uma margem bruta de 45% (porcento) quando o preço de #custo é menor ou igual a 100 reais quando o preço for maior que isso a margem bruta é de 35%.
#Escreva um programa que leia o preço de custo do produto e mostre na tela qual o seu preço de venda #com duas casas decimais.
preco_custo=float(input("Qual o preço de custo do produto: "))
if preco_custo >=100:
     preco_final=(preco_custo*0.35)+preco_custo
else:
     preco_final=(preco_custo*0.45)+preco_custo
print("A margem bruta é de: ",preco_final)
print("Gustavo Wendt")