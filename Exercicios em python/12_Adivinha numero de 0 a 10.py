#JOGO DO ADIVINHA O NUMERO DE 0 a 10

#Importando biblioteca random
import random

#Define uma variavel com o aleatorio de randint
sorteio = random.randint(0,10)

print('VAMOS BRINCAR DE ADIVINHA O NUMERO DE 0 a 10')
num = int(input('Informe um numero: '))
print('-'*20)
if sorteio == num:
    print('-'*20)
    print('Você acertou')
else:
    print('Você errou')
    print('-' * 20)
print('O numero foi {}'.format(sorteio))