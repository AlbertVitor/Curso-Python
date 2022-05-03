#Escreva um programa que leia um valor em metros e  exiba convertido em centimetros e melímetros.

m = float(input('Quantos metros? '))

cm = m * 100

mm = cm * 10

print('{} metros, {} centímetros {} milímetros.'.format(m, cm, mm))