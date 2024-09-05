sal = float(input('Qal é o salario do funcionario:  '))
novo = sal + (sal * 15 / 100)
print('Um funcionario que ganhava R${:.2f}, com o almento de 15%, passa a receber R${:.2f}.'.format(sal, novo))