cell = input('Введите клетку: ')
l = cell[:1]
n = int(cell[1:])
if l == 'a' or l == 'c' or l == 'e' or l == 'g':
    if n == 1 or n == 3 or n == 5 or n == 7:
        print('Чёрный')
    else:
        print('Белый')
elif l == 'b' or l == 'd' or l == 'f' or l == 'h':
    if n == 1 or n == 3 or n == 5 or n == 7:
        print('Белый')
    else:
        print('Чёрный')