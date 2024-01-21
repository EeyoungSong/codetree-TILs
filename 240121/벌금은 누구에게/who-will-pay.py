n, m, k = map(int, input().split())

arr = [0] * (n+1)
ans = -1

for _ in range(m):
    s = int(input())
    arr[s] += 1
    if arr[s] >= k:
        ans = s
        break

print(ans)