number = int(input())
if number % 10 == 1 and number != 11:
    print(number, 'попугай')
elif number % 10 == 2 or number % 10 == 3 or number % 10 == 4 and number !=12 and number != 13 and number != 14:
    print(number, "попугая")
else:
    print(number, "попугаев")

