n = int(input())
arr = list(map(int, input().split()))

s_arr = []
for i in range(n):
    s = arr[i]
    for j in range(i+1, n):
        if s + arr[j] < 0:
            break
        s += arr[j]
    s_arr.append(s)

print(max(s_arr))