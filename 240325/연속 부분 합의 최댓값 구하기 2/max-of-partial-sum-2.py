n = int(input())
arr = list(map(int, input().split()))

max_s = arr[0]
for i in range(n):
    s = arr[i]
    for j in range(i+1, n):
        if s + arr[j] < 0:
            break
        s += arr[j]
    max_s = max(s, max_s)

print(max_s)