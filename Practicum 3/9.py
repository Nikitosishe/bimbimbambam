ATT = int(input())
COMP = int(input())
YDS = int(input())
TD = int(input())
INT = int(input())
passer_rating = (((COMP/ATT - 0.3) * 5 + (YDS/ATT - 3) * 0.25  + (TD/ATT) * 20 + 2.375 - ((INT/ATT)*25))/6) * 100
print(passer_rating)