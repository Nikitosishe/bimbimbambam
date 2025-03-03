import math
N = int(input())
C = int(input())
number = int(input())
page_number = 1 + number // (N * C + 1)
C_number = math.ceil((number % (N * C + 1) + page_number - 1) / N)
N_number = math.ceil(number % (N * C + 1) + page_number - 1 - N * (C_number - 1))
print(f'страница {page_number} столбец {С_number} строка {N_number}')
