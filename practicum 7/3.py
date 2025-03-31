import math as mth
while True:
    number = float(input('Введите число: '))
    root = mth.sqrt(number)

    if root == int(root):
        print(f'Это число является полным квадратом')
        break
    else:
        print(f'Число не является полным квадратом, попробуйте ещё раз')
