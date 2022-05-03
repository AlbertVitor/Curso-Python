#Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto.

preço = float(input('Digite o valor do produto R$:'))

desconto = preço * 5/100
novoPreço = preço - desconto

print('O produto que custava R${:.2f} reais, na promoção com desconto de 5% vai custar R${:.2f} reais'.format(preço, novoPreço))