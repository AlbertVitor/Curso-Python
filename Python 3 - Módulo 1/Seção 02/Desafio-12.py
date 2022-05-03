#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

nome = input('Digite o nome do funcionário: ')
salario = float(input('Digite o salário deste funcionário: '))

aumento = salario * 15 / 100
novoSalario = aumento + salario

print('Um funcionário que ganhava R${:.2f} reais, com 15% de aumento, passa a receber R${:.2f} reais.'.format(salario, novoSalario)) 