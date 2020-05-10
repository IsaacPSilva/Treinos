numero = ('zero', 'um', 'dois', 'três', 'quarto', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
          'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
selecione = int(input('Informe um numero: '))
while selecione>20 or selecione<0:
    selecione = int(input('Tente novamente. Informe um numero: '))
ext = numero[selecione]
print(f'O numero informado foi {ext}')