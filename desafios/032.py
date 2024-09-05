from datetime import date
<<<<<<< HEAD
<<<<<<< HEAD
ano = int(input('Que ano quer analisar? '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))    
=======
=======
>>>>>>> 6b0f53541dfcfc40f0aea09f4ae61a6790573c19
ano = int(input('Que anao quer analizar?'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print('O ano {} é BIXESSTO'.format(ano))
else:
<<<<<<< HEAD
    print('O ano {} não é BIXESTO'.format(ano))    
>>>>>>> 6b0f53541dfcfc40f0aea09f4ae61a6790573c19
=======
    print('O ano {} não é BIXESTO'.format(ano))    
>>>>>>> 6b0f53541dfcfc40f0aea09f4ae61a6790573c19
