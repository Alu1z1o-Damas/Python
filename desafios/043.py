peso = float(input('Qual é o seu peso? (kg)'))
altura = float(input('Qual é sua altura? (m)')) 
imc = peso / (altura ** 2)
print('O seu IMC é de {:.1f}'.format(imc))
if imc < 18.5: 
    print('Você está abaixo do peso normal')
elif 18.5 <= imc < 25:
    print('Parabéns, você está na faixa de peso normal')  
elif 25 <= imc < 30:
    print('Você está em sobrepeso')
elif 30 <= imc < 40:
    print('Você está com Obesidade') 
elif imc >= 40:        
    print('Você está com Obesidade Mórbida, cuidado!')