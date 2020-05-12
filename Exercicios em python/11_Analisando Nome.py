nome = input('Informe seu nome: ')
print('-' * 20, '\nAnalisando nome...', '\n ')
print ('Seu nome com letras maiusculas é ',nome.upper())
print ('Seu nome com letras minusculas é ',nome.lower())
cont = nome.split()
print('Seu nome {} possui {} letras.'.format(cont[0], len(cont[0])))

