offset = 100000
MAX_NUM = 200000
arr = [''] * (MAX_NUM+1)

n = int(input())
p = 0

for _ in range(n):
    x, d = input().split()
    x = int(x)

    if d == 'L':
        for i in range(p, p-x, -1):
            arr[i+offset] = 'w'
        p = p - x + 1
    else:
        for i in range(p, p+x):
            arr[i+offset] = 'b'
        p = p + x - 1
        
print(arr.count('w'), arr.count('b'))