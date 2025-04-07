number = int(input())
i = 1
while i <= number:
    print(' ' * (number - i) + '*' * i)
    i += 1