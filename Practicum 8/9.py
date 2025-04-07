def is_prime(a):
    if a % 2 == 0:
        return a == 2
    d = 3
    while d * d <= a and a % d != 0:
        d += 2
    return d * d > a

number = int(input())
counter = 1
while counter <= number:
    if is_prime(counter) == True:
        print(counter)
    counter += 1