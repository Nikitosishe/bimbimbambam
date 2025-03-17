N = int(input())
a = N // 493
b = (N - a * 493) // 29
c = (N - a * 493) - b * 29
if a > 0:
    print(a, "галеонов")
if s > 0:
    print(b, "сиклей")
if c > 0:
    print(c, "кнатов")