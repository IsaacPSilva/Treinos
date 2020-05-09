print('--- CADASTRO ---')
idade = c = 0
cont = 's'
contIdade = contSexoMasc = contMulher = 0
while cont=='s':
    idade = int(input('Informe a idade: '))
    sexo = input('Informe o sexo [M/F]: ').lower()
    while sexo!='m' and sexo!='f' and sexo!='masculino' and sexo!='feminino':
        print('Opção Invalida, informe corretamente')
        sexo = input('Informe o sexo [M/F]: ')

    if idade>=18:
        contIdade += 1
    if sexo=='m' or sexo=='masculino':
        contSexoMasc += 1
    if (sexo=='f' or sexo=='feminino') and idade<20:
        contMulher += 1
    c+=1

    cont = input('Deseje continuar [S/N]: ').strip().lower()
    while cont!='s' and cont!='n':
        print('Opção invalida, informe corretamente')
        cont = input('Deseja continuar [S/N]: ').strip().lower()
print('-'*30)
print('CADASTRO DE PESSOAS - INFORMAÇÕES')
print('')
print(f'Quantidade de cadastrados: {c}')
print(f'Quantidade de homens cadastrado: {contSexoMasc}')
print(f'Quantidade de mulheres abaixo de 20 anos cadastrada: {contMulher}')