#Medidor de velocidade - 80 Limite


print('FISCALIZAÇÃO ELETRÔNICA - LIMITE DE VELOCIDADE 80 KM/H')
print('-'*40)
vel = int(input('Informe a velocidade registrada: '))
if vel <= 80:
    print('-' * 40)
    print('Sua velocidade está perfeito')
    print('-' * 40)
else:
    velAtual = vel - 80
    multa = velAtual * 7
    print('-' * 40)
    print('Você estava correndo acima da velocidade permitida \nSua velocidade passou {}km/h a mais \nSua multa será no valor de R${}.'.format(velAtual, multa))
    print('-'*40)