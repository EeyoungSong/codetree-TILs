import sys

n, s = map(int, input().split())
arr = list(map(int, input().split()))

ans = sys.maxsize

j = 0
for i in range(n):
    sum_val = 0
    for j in range(i, n):
        sum_val += arr[j]
        if sum_val >= s:
            ans = min(ans, j-i+1)
          
print(ans)