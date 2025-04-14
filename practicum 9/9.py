def total_dots_naive(N):
    total = 0
    for a in range(N + 1):
        for b in range(a, N + 1):
            total += a + b
    return total
N = int(input("Введите максимальное количество точек на плитке (N): "))
print(f"Суммарное количество точек на всех костях домино: {total_dots_simple(N)}")