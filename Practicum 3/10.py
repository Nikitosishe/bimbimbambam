x, y = map(int,input().split())
print(min(((x % y) + 1), ((y % x) + 1)))