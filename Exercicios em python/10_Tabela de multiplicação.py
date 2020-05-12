print('=-='*5)
print('{:^15}'.format('TABLE'))
print('=-='*5)
print()
while True:
    n = int(input('Enter a number for table (number < 0 to stop): '))
    if n < 0:
        break
    print(f'The table for {n} is:')
    for c in range(1, 11):
        print(f'{n:2} x {c:2} = {c * n}')
print('=-='*5)
print('End of execution.')