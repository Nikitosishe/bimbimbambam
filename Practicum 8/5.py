N = int(input())
counter = 0
sum = 0
for i in range(1, N):
    for j in range(1, N):
        if i % j == 0 and j != i:
            sum += j
    if sum == i:
        counter += 1
    sum = 0
print(counter)