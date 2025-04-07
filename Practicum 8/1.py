max_number = 0
while (i := int(input())) != -1:
    if max_number < i:
        max_number = i
print(max_number)