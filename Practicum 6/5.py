letters = ['a','b','c','d','e','f','g','h']
inf = input('Введите ход: ')
start, end = inf.split('-')
for i in range(8):
    if start[0] == letters[i]:
        if letters[i - 1] == end[0] or letters[i+1] == end[0]:
            if (int(start[1]) + 2 == int(end[1]) or
                    int(start[1]) - 2 == int(end[1])):
                print('Верно')
            else:
                print('Ошибка')
        elif letters[i - 2] == end[0] or letters[i + 2] == end[0]:
            if (int(start[1]) + 1 == int(end[1]) or
                    int(start[1]) - 1 == int(end[1])):
                print('Верно')
            else:
                print('Ошибка')