number_of_days = int(input())
if (number_of_days % 4 == 0 and number_of_days % 100 != 0) or number_of_days % 400 == 0:
    print(366)
else:
    print(365)
