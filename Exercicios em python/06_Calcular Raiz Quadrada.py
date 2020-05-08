### ATIVIDADE 02 - CALCULADOR RAIZ QUADRADA ###
print('CALCULADOR RAIZ QUADRADA')
num = int(input('Informe um valor: '))
if num < 0:
    print('Valor invalido')
else:
    tot = num ** 2
    print(f'A raiz quadrada de {num} é  {tot}.')