counter = 0
for i in range(100, 1000):
    if i % 17 == 0:
        print(i, end =' ')
        counter += 1
print(counter)