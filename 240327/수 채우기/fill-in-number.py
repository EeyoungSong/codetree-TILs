n = int(input())
cnt = 0

while n % 5 != 0:
    n -= 2
    cnt += 1

if n < 0:
    print(-1)

else:
    cnt += n // 5
    print(cnt)