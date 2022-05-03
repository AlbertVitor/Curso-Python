#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tint necessária para pintá-la
#Sabendo que cda litro de tinta pinta uma área de 2m²

largura = float(input('Digite a Largura da parede em metros: '))
altura = float(input('Digite a Altura da perede em metros: '))

area = largura * altura 
tinta = area / 2

print('A área de sua parede é {:.2f}m². \nA quantidade de tinta para pinta-la é {:.2f} Litros'.format(area, tinta))
