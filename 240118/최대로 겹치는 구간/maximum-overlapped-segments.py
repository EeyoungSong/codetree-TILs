MAX_NUM = 200
OFFSET = 100

n = int(input())
arr = [0] * MAX_NUM

for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, b):
        arr[i+OFFSET] += 1

print(max(arr))