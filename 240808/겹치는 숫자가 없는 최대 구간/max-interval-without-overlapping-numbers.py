n = int(input())
arr = [0] + list(map(int, input().split()))
count_arr = [0] * len(set(arr))

ans = 0
j = 0
for i in range(1, n+1):
    while j + 1 <= n and count_arr[arr[j+1]] == 0:
        count_arr[arr[j+1]] += 1
        j += 1
    
    ans = max(ans, j-i+1)
    count_arr[arr[i]] -= 1

print(ans)