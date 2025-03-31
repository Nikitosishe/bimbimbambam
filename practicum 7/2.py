input_str = list(input())
counter = 0
for i in input_str:
    counter += 1
    if counter % 3 == 0:
        print(i, end='')