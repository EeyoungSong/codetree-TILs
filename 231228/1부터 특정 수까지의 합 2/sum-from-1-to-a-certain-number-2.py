def func(s, n):
    if n <= 0:
        return s
    s += n
    return func(s, n-1)

s = 0
n = int(input())
print(func(s, n))