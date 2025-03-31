counter = 0
x = 0
while (t := float(input())) != 0:
    if t < x:
        counter += 1
x = t
print(counter)