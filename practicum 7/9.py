n, k, r = map(int, input().split(' '))
counter = 1
while r > n:
    n *= 1 + (k / 100)
    counter += 1
print(counter)