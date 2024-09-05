casa =float(input('Valor da casa: '))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamentos?'))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos '.format(casa, anos), end='')
print('A prestação será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')  
      