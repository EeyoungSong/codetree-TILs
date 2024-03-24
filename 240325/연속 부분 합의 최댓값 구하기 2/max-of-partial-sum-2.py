n = int(input())
arr = list(map(int, input().split()))

max_s = arr[0]
s = 0
for i in range(0, n):
    s += arr[i]
    max_s = max(s, max_s)
    if s < 0:
        s = 0    
        continue


print(max_s)