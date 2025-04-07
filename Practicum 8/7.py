while True:
    num = input(f'Введите число: ')
    if str.isdigit(num) == False:
        print('Ошибка. Попробуйте ещё раз')
    else:
        print(f'Введено целое число: {num}')
        break