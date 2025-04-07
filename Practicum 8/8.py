n1, n2, n3 = '', '', ''

#1
for i in range(1, 10):
    n1 += str(i)
    print(f'{n1} * 8 + {i} = {int(n1) * 8 + i}')
    print('\n')

#2
for j in range(1, 10):
    n2 += str(j)
    print(f'{n2} * 9 + {j + 1} = {int(n2) * 9 + (j + 1)}')
    print('\n')

#3
for n in range(1, 10):
    n3 += '1'
    print(f'{n3} * {n3} = {int(n3) ** 2}')
