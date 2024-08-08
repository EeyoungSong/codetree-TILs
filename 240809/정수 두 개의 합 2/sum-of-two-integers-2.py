n, k = map(int, input().split())
arr = [0]
for _ in range(n):
    arr.append(int(input()))

arr.sort()

j = 0
for i in range(1, n+1):
    while j != 1 and arr[i] + arr[j] > k:
        print(i, j)

    if j <= i:
        break
    
    ans += j-i