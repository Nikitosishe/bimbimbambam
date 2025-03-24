k = int(input('Введите количество: '))
counter = 0
for i in range(k):
    if k % 5 == 0 and k > 4:
        c+=1
    else:
        k -= 7
for j in range(k):
    if k % 7 == 0 and k > 6:
        counter += 1
    else:
        k -= 5
if counter > 0:
    print('да')
else:
    print('нет')