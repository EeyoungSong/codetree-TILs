MAX_NUM = 1000000
n, m = map(int, input().split())
arr_a = [0] * MAX_NUM
arr_b = [0] * MAX_NUM

def record(n, arr):
    at = 1
    for i in range(n):
        d, t = input().split()
        t = int(t)
        for _ in range(t):
            arr[at] = arr[at - 1] + (1 if d == 'R' else -1) 
            at += 1

    return arr, at

arr_a, time_a = record(n, arr_a)
arr_b, time_b = record(m, arr_b)

ans = -1
for i in range(1, time_a):
    if (arr_a[i] == arr_b[i]):
        ans = i
        break

print(ans)