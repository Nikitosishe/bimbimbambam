import math

while (i := int(input())) < 2:
    print('Введите число большее 2')
while i >= 2:
    i = math.sqrt(i)
    print('%.3f' % i)