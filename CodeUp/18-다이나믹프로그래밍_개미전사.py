n = int(input())
a = list(map(int, input().split()))

dp = [0 for i in range(300)]

dp[0] = a[0]
dp[1] = a[1]
for i in range(2, n):
    dp[i] = max(dp[i-2]+a[i], dp[i-1])
print(dp[n-1])
