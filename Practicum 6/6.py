data = input('Введите данные: ')
n, k, m = map(int, data.split(' '))
odin_krug = (n + k - 1) // k
total_time = odin_krug * 2 * m
print(total_time)
