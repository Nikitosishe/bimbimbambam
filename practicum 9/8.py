import math


def count_square_sums(x):
    count = 0
    max_a = int(math.isqrt(x))

    for a in range(1, max_a + 1):
        a_squared = a * a
        remaining = x - a_squared

        if remaining <= 0:
            continue

        b = math.isqrt(remaining)
        if b * b == remaining and b >= a:
            count += 1

    return count
x = int(input("Введите натуральное число x: "))
result = count_square_sums(x)
print(f"Количество способов представления числа {x} в виде суммы квадратов двух натуральных чисел: {result}")