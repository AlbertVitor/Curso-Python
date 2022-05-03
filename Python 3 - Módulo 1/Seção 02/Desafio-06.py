#Desenvolva um program que lei as duas notas de um aluno, calcule e mostre sua média

nome = input('Digite o nome do aluno: ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) /2

print('Aluno: {} \n Média: {}'.format(nome, media))