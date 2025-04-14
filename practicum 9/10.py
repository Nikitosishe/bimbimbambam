def count_staircases(N):
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    for m in range(N + 1):
        dp[0][m] = 1
    for k in range(1, N + 1):
        for m in range(1, N + 1):
            if m > k:
                dp[k][m] = dp[k][k]
            else:
                dp[k][m] = dp[k][m - 1] + dp[k - m][m - 1]
    return dp[N][N] - 1


N = int(input("Введите количество кубиков (N ≤ 100): "))
if N > 100:
    print("Ошибка: N должно быть ≤ 100")
else:
    print(f"Количество возможных лесенок: {count_staircases(N)}")