answer = int(input())
while answer % 2 == 0:
    answer //= 2
if answer == 1:
    print('верно')
else:
    print('неверно')