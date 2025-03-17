day_1 = int(input())
day_2 = int(input())
day_3 = int(input())
if day_1 == day_2 and day_1 != day_3:
    print(2)
elif day_2 == day_3 and day_2 != day_1:
    print(2)
elif day_2 == day_3 and day_2 == day_1:
    print(3)
else:
    print(0)
