n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)] 
dp[0][0] = grid[0][0]

for j in range(n-1):
    dp[0][j+1] = min(dp[0][j], grid[0][j+1])

for i in range(n-1):
    dp[i+1][0] = min(dp[i][0], grid[i+1][0])

for i in range(n-1):
    for j in range(n-1):
        dp[i+1][j+1] = min(max(dp[i+1][j], dp[i][j+1]), grid[i+1][j+1])

print(dp[n-1][n-1])