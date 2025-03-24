n, m = map(int, input().split('x'))
k = int(input())
counter = 0
if k % n == 0 or k % m == 0:
    print("Успешно")
else:
    print("Неосуществимо")
