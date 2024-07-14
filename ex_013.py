#013 Crie um algoritimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Qual o salário do funcionário? R$'))
reajuste = salario + (salario * 15 / 100)
print(f'Um funcionário que ganhava R${salario:.2f} com 15% de aumento passa a receber R${reajuste:.2f}.')