position = int(input('Введите порядковый номер цифры: '))
current_position = 1
if position == current_position:
    print(0)
current_position += 1
for number in range(1, 201):
    temp_number = number
    while temp_number > 0:
        digit = temp_number % 10
        temp_number //= 10
        if current_position == position:
            print(digit)
        current_position += 1