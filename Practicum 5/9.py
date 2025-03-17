n1, n2, n3 = map(int, data.split(' '))
a = max(n1, n2, n3)
b = min(n1, n2, n3)
if n1 != a and n1 != b:
    print(a, n1, b)
if n2 != a and n2 != b:
    print(a, n2, b)
if n3 != a and n3 != b:
    print(a, n3, b)