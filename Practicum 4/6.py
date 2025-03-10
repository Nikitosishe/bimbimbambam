score = input().split(':')
print(score)
if score[0] > score[1]:
    print(1)
elif score[1] > score[0]:
    print(2)
else:
    print(0)