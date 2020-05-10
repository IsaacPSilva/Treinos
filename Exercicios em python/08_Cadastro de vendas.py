print(' --- LOJAS ---')
cont = 's'
valor = totalGasto = preAlto = totAlto = menor =contProduto = 0
nomeMenor = ''
while cont == 's':
    #Detalhes do produto
    nome = input('Descrição produto: ')
    valor = float(input('Valor: '))
    #Total Gasto
    totalGasto += valor
    contProduto += 1
    #Valores maior de 1.000,00
    if valor>1000:
        totAlto += 1
    if valor>preAlto:
        preAlto = valor
    #Menor preço do produto
    if contProduto ==1:
        menor = valor
        nomeMenor = nome
    elif valor<menor:
        menor = valor
        nomeMenor=nome
    #Fim da problematica
    print('-'*20)
    cont = input('Vai continuar [S/N]: ')
    while cont!='s' and cont!='n':
        print('Opção invalida, tente novamente')
    print('-'*20)
print('DESCRIÇÃOS DOS PEDIDOS')
print(f'Valor total: R$ {totalGasto}')
print(f'Preço acima de R$ 1.000,00: {totAlto}')
print(f'Produto com menor preço: R$ {menor:.2f}.--- [{nomeMenor}]')
print('...')
print('Programa Finalizado')