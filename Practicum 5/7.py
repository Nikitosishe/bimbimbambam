N, K, M = map(int,input().split())
dis1 = (M - K) % N - 1
dis2 = (K - M) % N - 1
print(min(dis1, dis2))
