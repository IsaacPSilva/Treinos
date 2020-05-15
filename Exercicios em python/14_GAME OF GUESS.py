import random

print('-'*50)
print('{:^50}'.format("GAME OF GUESS"))
print('-'*50)
print('{:^50}'.format('Select 99 for exit game\n'))

#pontuação
pont_you = 0
pont_pc = 0

game = True

while game==True:
    number = random.randint(0,10)

    while True:

        you = int(input('Enter a number [0, 10]:  '))
        if you==99:
            game=False
            break

        while you<0 or you>10:
            you = int(input('Invalid value. Enter a number [0, 10]:  '))
            if you == 99:
                game=False
                break

        pc = random.randint(0,10)
        print(f'Your adversary selected {pc}.')
        print('-'*30)

        if you==number and pc!=number:
            pont_you = pont_you + 1
            print("You're right")
        elif pc == number and you!=number:
            pont_pc = pont_pc + 1
            print('Your adversary scored')

        elif you==number and pc==number:
            pont_you = pont_you + 1
            pont_pc = pont_pc + 1
            print('Both scored.')

        else:
            print('nobody scored')

        print(f'The number sorted: {number}')
        print('-=' * 15)
        print('')
        break


print(f'Your scored: {pont_you}')
print(f'Your adversary: {pont_pc}')

if pont_pc>pont_you:
    print('--- Your LOSS! ---')
elif pont_you>pont_pc:
    print('===  YOU WIN ===')
else:
    print('-=- Game Tied -=-')