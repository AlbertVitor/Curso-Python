#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
#Considere US$1,00 = R$5,02

reais = float(input('Quanto você tem na carteira? '))

cotacao = 5.02
coversao = reais / cotacao

print('Você tem {} Reais, e pode comprar {:.2f} Dólares'.format(reais, coversao))