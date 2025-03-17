N, K, M = map(int,input().split())
if M >= K:
    print(M - K - 1)
else:
    print(N - K - 1 + M)