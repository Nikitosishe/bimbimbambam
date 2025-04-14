counter = 0
while True:
    N = int(input())
    if N == 0:
        break
    if N % 2 and N >= 4:
        counter += 1
print(counter)